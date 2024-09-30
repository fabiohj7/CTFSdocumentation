from binascii import crc_hqx

from Crypto.Util.number import *

signature = 11846708563765925566960041185000169096696786507592449606097134515819715438558240779822408496104928523218582004731935742928920596211338788281244436953604948338760259319449210111508047522737044458081745094315916020050806865497732217231596805864532614317785839615400231231000593508683978615336646090629642389540748951611318831943860391027120162008399924921075032117477233471096050974400845455397412242066041787373808001695587019215237889960456906566702586133369568659093217638961697252121820070988664705760837399658925897884283968452584975523426673533375391658385796409511113386714544347398817200281938728306117670698459

n = 14769181878649942827894795888122567077978629020961894001708158701527598841919148906017822534741358021229674077077980651705461774935364521375309747020194266420486402687389203996030593754892050109923694442220979564776025326511508141355300082088181214910645475011993656328590961727035586327601000591600247232683031131961363124730152811245395918488095842771404333879308002522703682089653268774772781227980158818436030452502661096494522874250704483260085627116142682108075705813364295985958297630947882061619192475697505660547712008479987131635686652477683718558515922103354976216481639806632069595140594648248393355389689

p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 65537
tot = (p - 1) * (q - 1)
d = pow(e, -1, tot)
