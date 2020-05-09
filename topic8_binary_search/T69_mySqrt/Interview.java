
import java.util.*;


public class Interview {

	public int mySqrt(int x) {
		if(x==1){
			return x;
		}
		int l =0;
		int r =x/2;
		while(l<=r){
			int mid = l+(r-l)/2;
			if((long) mid*mid<=x){
				l=mid+1;
			}else{
				r=mid-1;
			}			
		}
		return l-1;

    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        //System.out.println("璇疯緭鍏ヤ换鎰忔暟鎹�娉ㄦ剰杈撳叆鏁版嵁鐨勪釜鏁板繀椤诲ぇ浜庣瓑浜庨渶瑕佽浆鍖栫殑涓暟)锛�);
        String str = scan.nextLine();

        int a = Integer.parseInt(str);
        Interview interview = new Interview();
        int res = interview.mySqrt(a);
        System.out.println(res);
    }

}
