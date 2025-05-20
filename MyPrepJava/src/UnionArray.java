import java.util.ArrayList;
import java.util.List;

public class UnionArray {
    List<Integer> unionArray(int[] arr1, int[] arr2){
        int i=0,j=0;
        int n1=arr1.length, n2 = arr2.length;
        List<Integer> union = new ArrayList<>();
        while(i<n1 && j<n2) {
            if (arr1[i] <= arr2[j]) {
                if (union.isEmpty() || union.get(union.size() - 1) != arr1[i])
                    union.add(arr1[i]);
                i++;
            } else {
                if (union.isEmpty() || union.get(union.size() - 1) != arr2[j])
                    union.add(arr2[j]);
                j++;
            }
        }
            while(i<n1){
                    if(union.isEmpty() ||union.get(union.size()-1)!=arr1[i])
                        union.add(arr1[i]);
                    i++;

            }
            while(j<n2){
                if(union.isEmpty() || union.get(union.size()-1)!=arr2[j])
                    union.add(arr2[j]);
                j++;
            }

        return union;
    }
    public static void main(String[] args) {
        int arr1[]= {1,1,2,2,3,4,5};
        int arr2[]= {1,2,3,3,4};
        UnionArray u = new UnionArray();
        List<Integer> list = u.unionArray(arr1,arr2);
    }
}
