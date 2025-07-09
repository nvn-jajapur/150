public class MultiThread {

    public static class Sample implements Runnable {

        @Override
        public void run() {
            System.out.println("Thread started" + " " +Thread.currentThread().getName()+" " + System.currentTimeMillis());
            System.out.println("Thread Stooped" + " " +Thread.currentThread().getName()+" "+ System.currentTimeMillis());
        }
    }


    public static void main(String[] args) {
        Thread firstThread = new Thread( new Sample(), "1");
        firstThread.start();
        Thread secondThread = new Thread( new Sample(), "2");
        secondThread.start();

    }
}