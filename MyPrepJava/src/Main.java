import javax.swing.*;
import java.util.ArrayList;
import java.util.List;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {

    void mergeSort(List<Integer> arr, int low, int high){
        int mid = (low + high)/2;
        if (low>=high)
            return;
        mergeSort(arr, low, mid);
        mergeSort(arr,mid+1, high);
        merge(arr, low, mid, high);
    }
    void merge(List<Integer> arr, int low, int mid, int high){
        int left = low, right = mid+1;
        List<Integer> temp = new ArrayList<>();
        while(left<=mid && right<=high) {
            if (arr.get(left) <=arr.get(right)) {
                temp.add(arr.get(left));
                left++;
            } else {
                temp.add(arr.get(right));
                right++;
            }
        }
        while (left<=mid){
            temp.add(arr.get(left));
            left++;
        }
        while (right<=high){
            temp.add(arr.get(right));
            right++;
        }
        System.out.println(temp);

        for (int i = 0; i < temp.size(); i++) {
        arr.set(low + i, temp.get(i));
    }
    }

    public static void main(String[] args) {
        Main m = new Main();
    List<Integer> list = new ArrayList<>();
    list.add(3);
    list.add(5); list.add(1); list.add(9);  list.add(0);
    m.mergeSort(list,0, list.size()-1);
    System.out.println(list);
    }
}