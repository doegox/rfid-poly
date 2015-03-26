Seriously needed:
For PC/SC support you'll need pyscard. (For Debian Linux users you will also need to install PCSC-Lite)
Here are the links to download:
pyscard: http://sourceforge.net/projects/pyscard/files/
PCSC-Lite: https://alioth.debian.org/frs/?group_id=30105

Optional:(to make the debug text colorful)
The debian linux users can skip this one, for windows XP users you will need to install another package:
http://newcenturycomputers.net/projects/wconio.html

Our software now supports the following readers and you will need to install drivers to make them work:
Reader                                                             Download link
TOUCHATAG                                                   http://www.touchatag.com/downloads
OMNIKEY CardMan 5321                                http://www.hidglobal.com/technology.php?tech_cat=19&subcat_id=10&headerType=1
ARYGON                                                          http://www.arygon.de/index.php?option=com_content&view=article&id=185%3Anfc-mifare-desktop-reader&catid=43%3Ahf-reader&Itemid=81&lang=en

Remark: 
1.For OMNIKEY CardMan 5321, the manufacturer hasn't registered the contactless interface reader for pcsc, so you need to install the manufacturer driver instead.
For the details please look at: http://wiki.yobi.be/wiki/RFID

2.The driver for ARYGON reader can not be installed on debian Linux, so our software doesn't implement the ARYGON on Debian Linux.