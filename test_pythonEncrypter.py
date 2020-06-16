from unittest import TestCase
import pythonEncrypter

class Test(TestCase):
    def test_decrypt_message1(self):
        date = "21/11/1976"
        message = ";jsadjfahs;fjsfjs a; 'afj a'jf'aejfa'efj3920293  a9 e9af' 'q39 a9e9 'a eq23qw-==1=1 wfsfsJ[[ "
        self.assertEqual(pythonEncrypter.decryptMessage(pythonEncrypter.encryptMessage(message, date),date), message)
    def test_decrypt_message2(self):
        date = "11/05/1986"
        message = ";jsadjfahs;fjsfjs SSJWJLWWLL  LWLWLWL LW LWLW AAP PP020U3W;AFJ; ASF90293A;F 02930  SA'AF]AF]a; 'afj a'jf'aejfa'efj3920293  a9 e9af' 'q39 a9e9 'a eq23qw-==1=1 wfsfs[[ qwertyuicvbnm,1234567890)(*&^%$#@!"
        self.assertEqual(pythonEncrypter.decryptMessage(pythonEncrypter.encryptMessage(message, date),date), message)
    def test_decrypt_message3(self):
        date = "01/11/1900"
        message = ";A;HFHAFSJ;AFDSJ;AFS;Jjsadjfahs;fjWWJL;WJWLJRWJRLWJ99922717191  JJAJ;AFJ;F;JS J;;J AS;LKASFJ A;;)(*&^%$#@    !@#$%^&*(KJHG   FZXCVB}?{>{<AFsfjs    SSJWJLWWLL  LWLWLWL LW LWLW AAP PP020U3W;AFJ; ASF90293A;F 02930  SA'AF]AF]a; 'afj a'jf'aejfa'efj3920293  a9 e9af' 'q39 a9e9 'a eq23qw-==1=1 wfsfs[[ "
        self.assertEqual(pythonEncrypter.decryptMessage(pythonEncrypter.encryptMessage(message, date),date), message)
    def test_decrypt_message4(self):
        date = "13/01/1999"
        message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        self.assertEqual(pythonEncrypter.decryptMessage(pythonEncrypter.encryptMessage(message, date),date), message)
    def test_decrypt_message5(self):
        date = "23/05/1980"
        message = ";HELLO HOW AAWRE  YOU THE BES :A;00U22U ;SFAJF~!@#$   %^&*()(*&^%$#   @!ZXCVBNM<Pjsadjfahs;fjsfjs     SSJWJLWWLL  LWLWLWL LW LWLW AAP PP020U3W;AFJ; ASF90293A;F 02930  SA'AF]AF]a; 'afj a'jf'aejfa'efj3920293  a9 e9af' 'q39 a9e9 'a eq23qw-==1=1 wfsfs[[ "
        self.assertEqual(pythonEncrypter.decryptMessage(pythonEncrypter.encryptMessage(message, date),date), message)
    def test_decrypt_message6(self):
        date = "22/05/2002"
        message = ";jsadjfahs;fjsfjs SSJWA'A''AA'A''AA'A'AJF'JA'J A'JA JA 'AJ 'AJ'EJ3'EJA3'AJEAOEAJOEAJEA'AEJEAJ'EAEJEAEJ E AJPEJIOY29Y983YOW0H0JEF AJ;AE ;DFJJLWWLL  LWLWLWL LW LWLW AAP PP020U3W;AFJ; ASF90293A;F 02930  SA'AF]AF]a; 'afj a'jf'aejfa'efj3920293  a9 e9af' 'q39 a9e9 'a eq23qw-==1=1 wfsfs[[ "
        self.assertEqual(pythonEncrypter.decryptMessage(pythonEncrypter.encryptMessage(message, date),date), message)
    def test_decrypt_message7(self):
        date = "21/06/2001"
        message = ";JAF;AFLJAF  LA;ADFS JLKAFSJLJ2I3222  IOSLAJ;823Y492(&*&$(^(&      )&)&^*%*$&*(^)^) ) )* )& )&) *) * ^)^ )^ $*$ (^ )&;jsadjfahs;fjsfjs SSJWJLWWLL  LWLWLWL LW LWLW AAP PP020U3W;AFJ; ASF90293A;F 02930  SA'AF]AF]a; 'afj a'jf'aejfa'efj3920293  a9 e9af' 'q39 a9e9 'a eq23qw-==1=1 wfsfs[[ "
        self.assertEqual(pythonEncrypter.decryptMessage(pythonEncrypter.encryptMessage(message, date),date), message)
    def test_decrypt_message8(self):
        date = "01/12/1966"
        message = ";AJF;A'JAA''JASFJKSFDJS ;A SDJ' AFS;J ADFS'AS ;JFPJO293SEPFAJES' PFAS 'FAUS0 A0 A0F203 AOF jsadjfahs;fjsfjs SSJWJLWWLL  LWLWLWL LW LWLW AAP PP020U3W;AFJ; ASF90293A;F 02930  SA'AF]AF]a; 'afj a'jf'aejfa'efj3920293  a9 e9af' 'q39 a9e9 'a eq23qw-==1=1 wfsfs[[ "
        self.assertEqual(pythonEncrypter.decryptMessage(pythonEncrypter.encryptMessage(message, date),date), message)
    def test_decrypt_message9(self):
        date = "13/12/1970"
        message = "JAJJL ;A DS0 DSF0AS F092309r ja ' r'a rj;ja '3j ja'faj'aj'[] ]]  ;jsadjfahs;fjsfjs SSJWJLWWLL  LWLWLWL LW LWLW AAP PP020U3W;AFJ; ASF90293A;F 02930  SA'AF]AF]a; 'afj a'jf'aejfa'efj3920293  a9 e9af' 'q39 a9e9 'a eq23qw-==1=1 wfsfs[[ "
        self.assertEqual(pythonEncrypter.decryptMessage(pythonEncrypter.encryptMessage(message, date),date), message)
    def test_decrypt_message10(self):
        date = "11/11/1977"
        message = ":J: Jf;ajs;jf a;jd;fla93023h9 0a0e9fue90 9asf9a0s f9as0 f90as 90faus f09a s[f;jsadjfahs;fjsfjs SSJWJLWWLL  LWLWLWL LW LWLW AAP PP020U3W;AFJ; ASF90293A;F 02930  SA'AF]AF]a; 'afj a'jf'aejfa'efj3920293  a9 e9af' 'q39 a9e9 'a eq23qw-==1=1 wfsfs[[ "
        self.assertEqual(pythonEncrypter.decryptMessage(pythonEncrypter.encryptMessage(message, date),date), message)
