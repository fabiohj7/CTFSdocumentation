import java.util.Base64;

public class flag{

  int i = 275;
  int i2 = 306;
  int i3 = 42;

  public static void main(String[] args)
  {
    obf(275, 306, 42);

  }

  public static String obf(int i, int i2, int i3) {
    int i4 = i2 - i;
    byte[] theFlag;
    String notTheFlag = "bEVYCkNEWV5LRElPBgpFRApeQk8KWkZLRE9eCm9LWF5CBgpHS0QKQktOCktGXUtTWQpLWVlfR09OCl5CS14KQk8KXUtZCkdFWE8KQ0ReT0ZGQ01PRF4KXkJLRApORUZaQkNEWQpIT0lLX1lPCkJPCkJLTgpLSUJDT1xPTgpZRQpHX0lCCgcKXkJPCl1CT09GBgpkT10Kc0VYQQYKXUtYWQpLRE4KWUUKRUQKBwpdQkNGWV4KS0ZGCl5CTwpORUZaQkNEWQpCS04KT1xPWApORURPCl1LWQpHX0lBCktIRV9eCkNECl5CTwpdS15PWApCS1xDRE0KSwpNRUVOCl5DR08ECmhfXgpJRURcT1hZT0ZTBgpJWUtdSV5MUU5TRB5HG0l1RkUeTk94WXVYdUxfZAtXIF5CTwpORUZaQkNEWQpCS04KS0ZdS1NZCkhPRkNPXE9OCl5CS14KXkJPUwpdT1hPCkxLWApHRVhPCkNEXk9GRkNNT0ReCl5CS0QKR0tECgcKTEVYClpYT0lDWU9GUwpeQk8KWUtHTwpYT0tZRURZBA==";
    
    theFlag = Base64.getDecoder().decode(notTheFlag);

    char[] cArr = new char[i4];
    for (int i5 = 0; i5 < i4; i5++) {
      cArr[i5] = (char) (theFlag[i + i5] ^ i3);
    }
    System.out.println(cArr);
    return new String(cArr);
  }
}
