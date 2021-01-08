import java.util.Random;

public class QSort{
    private void swap(long[] arr, int a, int b){
	if( a == b){
	    return;
	}
	if (arr[a] == arr[b]){
	    return;
	}
	long valueA = arr[a];
	arr[a] = arr[b];
	arr[b] = valueA;
	return;
    }
    public void sort(long[] arr, int from, int to){
	/*	System.out.println("\nDebug#L17:from="+from+",to="+to);
	for(long x:arr){
	    System.out.print(x+ " ");
	}*/
	//	System.out.println();
	if(from >= to){
	    return;
	}
	if((from + 1) == to){
	    if( arr[from] > arr[to]){
		this.swap(arr, from , to);
	    }
	    return;
	}
	long threshold = arr[from];
	int fromIndex = from + 1;
	int toIndex = to;
	while(fromIndex < toIndex){
	    for(; fromIndex < toIndex; fromIndex++){
		if(arr[fromIndex] > threshold){
		    break;
		}
	    }
	    if(fromIndex >= toIndex){
		break;
	    }
	    for(; fromIndex < toIndex; toIndex--){
		if(arr[toIndex] <= threshold){
		    break;
		}
	    }
	    if(fromIndex >= toIndex){
		break;
	    }
	    if(fromIndex < toIndex){
		this.swap(arr, fromIndex, toIndex);
		fromIndex++;
		toIndex--;
	    }
	}
	if(arr[fromIndex] < threshold){
	    arr[from] = arr[fromIndex];
	    arr[fromIndex] = threshold;
	    this.sort(arr, from, fromIndex - 1);
	    this.sort(arr, fromIndex +1, to);
	    return;
	}
	if(arr[fromIndex] >= threshold){
	    //no need to swap
	    this.sort(arr, from, fromIndex -1);
	    this.sort(arr, fromIndex + 1, to);
	    return;
	}
    }
    
    public static void main(String[] args){
	QSort q = new QSort();

	Random r = new Random();
	int length = 500;
	long[] arr = new long[length];
	for(int i = 0 ;i < length; i++){
	    arr[i] = r.nextInt(0x123);
	    System.out.print(arr[i] + " ");
	}
	System.out.println();
		/*
	for(int i = 0 ;i < length; i++){
	    System.out.print(arr[i] + " ");
	}
	System.out.println("\n\n");*/
	

	q.sort(arr, 0, length -1);
	
	for(int i = 0 ;i < length; i++){
	    System.out.print(arr[i] + " ");
	}
	System.out.println();
	/*
	long[] arr= {4288, 4305, 2199, 3590, 1093};

	q.sort(arr, 0, 4);
	for(long x: arr){
	    System.out.println(x);
	}*/
	    
    }
}
