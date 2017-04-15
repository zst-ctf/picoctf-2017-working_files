import java.util.Base64.Decoder;

public class freeThePicklesHacked {
  
  public static String get_flag() { String str1 = "Hint: Don't worry about the schematics";
    String str2 = "eux_Z]\\ayiqlog`s^hvnmwr[cpftbkjd";
    String str3 = "Zf91XhR7fa=ZVH2H=QlbvdHJx5omN2xc";
    byte[] arrayOfByte1 = str2.getBytes();
    byte[] arrayOfByte2 = str3.getBytes();
    byte[] arrayOfByte3 = new byte[arrayOfByte2.length];
    for (int i = 0; i < arrayOfByte2.length; i++)
    {
      arrayOfByte3[i] = arrayOfByte2[(arrayOfByte1[i] - 90)];
    }
    System.out.println(java.util.Arrays.toString(java.util.Base64.getDecoder().decode(arrayOfByte3)));
    return new String(java.util.Base64.getDecoder().decode(arrayOfByte3));
  }
  
  public static void main(String[] paramArrayOfString) {
    // Comment away this: System.out.println("Nothing to see here");
    // replace with get_flag()
    get_flag();
  }
}

// To compile:
// javac freeThePicklesHacked.java
// jar cmvf META-INF/MANIFEST.MF freeThePicklesHacked.jar freeThePicklesHacked.class
// java -jar ./freeThePicklesHacked.jar

// Output is a byte array, use https://cryptii.com/decimal/text to convert to ASCII
// flag_{pretty_cool_huh}