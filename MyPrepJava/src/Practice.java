import java.util.*;

public class Practice {
    public static void main(String[] args) {
//        int arr[] = new int[10];
//        Arrays.fill(arr,2);
//        for(int i : arr) {
//            arr[i]=i;
//            System.out.println(i);
//        }
//        for(int i : arr) {
//            System.out.println(arr[i]);
//        }
//        int mat[][] = new int[5][5];
//        for( int i=0;i < 5; i++){
//            for( int j=0;j<5;j++){
//                mat[i][j] +=1;
////                System.out.println(mat[i][j]);
//            }
//        }
//        for( int i=0;i < 5; i++){
//            for( int j=0;j<5;j++){
////                mat[i][j] +=1;
//                System.out.print(mat[i][j]);
//            }
//            System.out.println();
//        }
//        int[] sample = {2,4,0,2,9,10};
//        Arrays.sort(sample);
//        System.out.println(Arrays.binarySearch(sample, 100));
//        String str ="Naveen";
//        for( int i=0; i<5;i++){
//            String str2 = str + i;
//            System.out.println(str2 + " " + System.identityHashCode(str2));
//        }
//        StringBuffer s = new StringBuffer("Naveen");
//        for (int i=0;i<5;i++){
//            s.append(i);
//            System.out.println(System.identityHashCode(s));
//        }
//        List<Integer> list = new ArrayList<>();
//        for( int i=0; i<5;i++){
//        list.add(i);}
//        list.set(list.size()-1,10);
//        list.remove(4);
//        for(int t: list){
//            System.out.println(list.get(t));
//        }
//        LinkedList<Integer> list = new LinkedList<>();
//        list.push(1);
//        list.push(2);
//        list.push(2);
//        int x = list.peek();
//        int y = list.poll();
//        System.out.println(x + " " + y+" " + list.size()) ;
        Set<String> set = new HashSet<>();
        set.add("Naveen");
        set.add("naveen");
        set.add("apple");
        set.add("z");
        Set<String> set2 = new LinkedHashSet<>();
        set2.add("Naveen");
        set2.add("naveen");
        set2.add("apple");
        set2.add("z");

        Set<String> set3 = new TreeSet<>();
        set3.add("Naveen");
        set3.add("naveen");
        set3.add("apple");
        set3.add("z");

        SortedSet<String> set4 = new TreeSet<>();
        set4.add("Naveen".toLowerCase());
        set4.add("naveen");
        set4.add("apple");
        set4.add("z");
        Iterator i = set.iterator();
        Iterator j = set2.iterator();
        Iterator k = set3.iterator();
        Iterator l = set4.iterator();
        while(i.hasNext()){
            System.out.println(i.next());
        }
        while(j.hasNext()){
            System.out.println(j.next());
        }

        while(k.hasNext()){
            System.out.println(k.next());
        }
        while(l.hasNext()){
            System.out.println(l.next());
        }
        for( String s : set4){
            System.out.println(s);
        }




    }
}
