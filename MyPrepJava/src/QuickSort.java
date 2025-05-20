import java.util.ArrayList;
import java.util.List;

public class QuickSort {


    void quicksort(List<Integer> list, int low, int high){
        if(low<high){
            int index = partition(list, low,high);
            quicksort(list,low,index-1);
            quicksort(list,index+1,high);
        }
    }
    int partition(List<Integer> list, int low, int high){
        int pivot = list.get(low);
        int i=low, j=high;
        while(i<j){
            while(list.get(i)<=pivot && i<=high-1){
                i++;
            }
            while(list.get(j) >pivot && j>=low+1){
                j--;
            }
            if(i<j){
                int temp=list.get(j);
                list.set(j, list.get(i));
                list.set(i,temp);
            }
        }
        int temp=list.get(j);
        list.set(j, list.get(low));
        list.set(low,temp);
        return j;
    }
    public static void main(String[] args){
        QuickSort q = new QuickSort();
        List<Integer> list = new ArrayList<>();
        list.add(3);
        list.add(5); list.add(1); list.add(9);  list.add(0);
        q.quicksort(list,0,list.size()-1);
        System.out.println(list);
    }
}
