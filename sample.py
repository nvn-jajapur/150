import paramiko
import os
import logging
import tempfile
from dotenv import load_dotenv

# --- Configuration ---
load_dotenv()  # Load environment variables from .env file

SOURCE_SERVER_IP =  "10.198.19.00"#os.getenv("SOURCE_SERVER_IP")
DEST_SERVER_IP = os.getenv("DEST_SERVER_IP")
USERNAME = "shiiva-reddy"#os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
SOURCE_PATH = os.getenv("SOURCE_PATH")
DEST_PATH = os.getenv("DEST_PATH")

# --- Logging setup ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("data_transfer.log"),
        logging.StreamHandler()
    ]
)

def connect_ssh(hostname, username, password=None, key_filename=None):
    """Establishes an SSH connection."""
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if key_filename:
            client.connect(hostname, username=username, key_filename=key_filename)
        else:
            client.connect(hostname, username=username, password=password)
        logging.info(f"Successfully connected to SSH on {hostname}")
        return client
    except paramiko.AuthenticationException:
        logging.error(f"Authentication failed for {username}@{hostname}. Check credentials.")
    except paramiko.SSHException as e:
        logging.error(f"SSH connection failed to {hostname}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error connecting to {hostname}: {e}")
    return None

def transfer_data_sftp(source_client, dest_client, source_path, dest_path):
    """Transfers files recursively from source to destination using SFTP."""
    try:
        sftp_source = source_client.open_sftp()
        sftp_dest = dest_client.open_sftp()

        try:
            sftp_dest.stat(dest_path)
        except IOError:
            logging.info(f"Destination directory {dest_path} does not exist. Creating it...")
            sftp_dest.mkdir(dest_path)

        items = sftp_source.listdir(source_path)
        logging.info(f"Found {len(items)} items in source: {source_path}")

        for item in items:
            source_item_path = os.path.join(source_path, item).replace("\\", "/")
            dest_item_path = os.path.join(dest_path, item).replace("\\", "/")

            try:
                mode = sftp_source.stat(source_item_path).st_mode
                if mode & 0o040000:  # Directory
                    logging.info(f"Entering directory: {source_item_path}")
                    try:
                        sftp_dest.mkdir(dest_item_path)
                        logging.info(f"Created directory: {dest_item_path}")
                    except IOError as e:
                        if "File exists" not in str(e):
                            logging.warning(f"Could not create directory: {dest_item_path} - {e}")
                    transfer_data_sftp_recursive(source_client, dest_client, source_item_path, dest_item_path, sftp_source, sftp_dest)
                else:  # File
                    temp_file = os.path.join(tempfile.gettempdir(), f"{item}_temp")
                    sftp_source.get(source_item_path, temp_file)
                    sftp_dest.put(temp_file, dest_item_path)
                    os.remove(temp_file)
                    logging.info(f"Transferred file: {item}")
            except Exception as e:
                logging.error(f"Error transferring item {item}: {e}")

    except Exception as e:
        logging.error(f"SFTP error: {e}")
        return False
    finally:
        if 'sftp_source' in locals():
            sftp_source.close()
        if 'sftp_dest' in locals():
            sftp_dest.close()
        logging.info("SFTP connections closed.")
    return True

def transfer_data_sftp_recursive(source_client, dest_client, source_dir, dest_dir, sftp_source, sftp_dest):
    """Recursively transfers directories and files."""
    for item in sftp_source.listdir(source_dir):
        source_item_path = os.path.join(source_dir, item).replace("\\", "/")
        dest_item_path = os.path.join(dest_dir, item).replace("\\", "/")

        try:
            mode = sftp_source.stat(source_item_path).st_mode
            if mode & 0o040000:  # Directory
                try:
                    sftp_dest.mkdir(dest_item_path)
                    logging.info(f"Created directory (recursive): {dest_item_path}")
                except IOError as e:
                    if "File exists" not in str(e):
                        logging.warning(f"Could not create directory: {dest_item_path} - {e}")
                transfer_data_sftp_recursive(source_client, dest_client, source_item_path, dest_item_path, sftp_source, sftp_dest)
            else:  # File
                temp_file = os.path.join(tempfile.gettempdir(), f"{item}_temp")
                sftp_source.get(source_item_path, temp_file)
                sftp_dest.put(temp_file, dest_item_path)
                os.remove(temp_file)
                logging.info(f"Transferred file (recursive): {item}")
        except Exception as e:
            logging.error(f"Error processing {item}: {e}")

def main():
    logging.info("Starting data transfer...")

    source_client = connect_ssh(SOURCE_SERVER_IP, USERNAME, PASSWORD)
    if not source_client:
        logging.error("Failed to connect to source server.")
        return

    dest_client = connect_ssh(DEST_SERVER_IP, USERNAME, PASSWORD)
    if not dest_client:
        logging.error("Failed to connect to destination server.")
        source_client.close()
        return

    logging.info(f"Transferring from {SOURCE_SERVER_IP}:{SOURCE_PATH} to {DEST_SERVER_IP}:{DEST_PATH}")
    success = transfer_data_sftp(source_client, dest_client, SOURCE_PATH, DEST_PATH)

    if success:
        logging.info("Data transfer completed successfully.")
    else:
        logging.error("Data transfer failed.")

    source_client.close()
    dest_client.close()
    logging.info("SSH connections closed.")

if __name__ == "__main__":
    main()


