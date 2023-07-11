public class secLargestNumber {
    private int[] array;
    secLargestNumber(int[] array){
        this.array = array;
    }
    public int findNum(){
        int max = Integer.MIN_VALUE;
        int second_max = Integer.MIN_VALUE;

        for(int num: array){
            if (num > max){
                second_max = max;
                max = num;
            }else if(num > second_max && num < max){
                second_max = num;
            }
        }
        return second_max;
    }
    public static void main(String[] args) {
        int [] arr = {7,3,9,9,2,6,7,3,1};
        secLargestNumber ans = new secLargestNumber(arr);
        int answer = ans.findNum();
        System.out.println(answer);
    }
}

// The second question was to find the second largest element in an unsorted array that contained 
// duplicate elements. I did it in O(n) TC and O(1) SC. 
