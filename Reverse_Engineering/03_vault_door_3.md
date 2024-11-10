# vault door 3

flag: `picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_1fb380}`

my approach to the problem:
- this is another problem which checks the password
- ```
    import java.util.*;

    class VaultDoor3 {
    public static void main(String args[]) {
    VaultDoor3 vaultDoor = new VaultDoor3();
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter vault password: ");
    String userInput = scanner.next();
    String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
    if (vaultDoor.checkPassword(input)) {
    System.out.println("Access granted.");
    } else {
    System.out.println("Access denied!");
    }
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18gb41_u_4_mfr340");
    }
    }
  
    ```
-  this code checks for the password:
    1. an array of 32 characters is created to rearrange the password.
    2. For the first 8 characters, it copies them from the password.
    3. For the next 8 characters from 8 to 15 , it copies characters from a reversing index.
    4. for the rest , it fills it in a pattern based on even and odd indices

- ```
    target = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"
    password = [''] * 32
    
    for i in range(8):
    password[i] = target[i]
    
    
    for i in range(8, 16):
    password[23 - i] = target[i]
    
    
    for i in range(16, 32, 2):
    password[46 - i] = target[i]
    
    
    for i in range(31, 16, -2):
    password[i] = target[i]
    
    
    password_str = ''.join(password)
    print("The password is:", password_str)
  ```
- this code allows you to find the password