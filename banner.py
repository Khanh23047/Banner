import time
from time import strftime
import os
import sys
import requests
import json
from time import sleep
from datetime import datetime, timedelta
import base64
import subprocess
from pystyle import Colors, Colorate

def banner():
    banner = f"""
██████╗░██╗░░░██╗████████╗░█████╗░░█████╗░██╗░░░░░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
██████╔╝╚██╗░██╔╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
██╔══██╗░╚████╔╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░
██║░░██║░░╚██╔╝░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝

TOOL BY: DUY KHÁNH             PHIÊN BẢN : 3.0
════════════════════════════════════════════════  
[</>] BOX ZALO : https://zalo.me/g/nguadz335
[</>] KÊNH YOUTUBE : REVIEWTOOL247NDK
[</>] ADMIN TOOL : DUYKHANH
❤ CHÀO MỪNG BẠN ĐÃ ĐẾN VỚI TOOL ❤
════════════════════════════════════════════════  
                  [THÔNG BÁO]
>>>>TOOL ĐANG TRONG QUÁ TRÌNH PHÁT TRIỂN THÊM<<<<   
❗MUA KEY VIP LIÊN HỆ ADMIN CHỈ 700đ/ 1 DAY❗  
════════════════════════════════════════════════                                
"""

    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)

os.system("cls" if os.name == "nt" else "clear")
banner()
print ("╔═════════════════════╗")
print ("║  Tool Trao Đổi Sub  ║")
print ("╚═════════════════════╝")
print("[</>] Nhập Số [1.1] TDS TIKTOK >>CLICK<< ")
print("[</>] Nhập Số [1.2] TDS TIKTOK & TIKTOK NOW >>CLICK<<")
print("[</>] Nhập Số [1.3] TDS Facebook V1 >>VIP<< ")
print("[</>] Nhập Số [1.4] TDS Facebook V2 >>VIP<<")
print("[</>] Nhập Số [1.5] TOOL ĐỔI MK TĐS >>ON<<")

print("════════════════════════════════════════════════  ")
print ("╔═════════════════════╗")
print ("║ Tool Tương Tác Chéo ║")
print ("╚═════════════════════╝")
print("[</>] Nhập Số [2.1] TTC FACEBOOK >>VIP<<")

print("════════════════════════════════════════════════  ")
print ("╔════════════════════════╗")
print ("║Tool Tiện Ích Facebook  ║")
print ("╚════════════════════════╝")
print("[</>] Nhập Số [3.1] Tool Reg Page >>ON<<")
print("[</>] Nhập Số [3.2] Tool Reg Nick Facebook NVR >>ON<<")
print("[</>] Nhập Số [3.3] Tool Tạo Mail 10P >>ON<<")
print("[</>] Nhập Số [3.4] Tool Share Ảo Cookie >>ON<<")
print("[</>] Nhập Số [3.5] Tool Get ID >>ON<<")

print("════════════════════════════════════════════════  ")
print ("╔═══════════════════╗")
print ("║    TOOL NGHỊCH    ║")
print ("╚═══════════════════╝")
print("[</>] Nhập Số [4.1] Tool Tài Xỉu >>ON<<")
print("[</>] Nhập Số [4.2] Tool Tài Xỉu [MD5] >>ON<<")
print("[</>] Nhập Số [4.3] Tool Fake CCCD >>VIP<<")
print("[</>] Nhập Số [4.4] Tool Spam SMS >>VIP<<")
print("[</>] Nhập Số [4.5] Tool Buff TikTok >>ON<<")
print("[</>] Nhập Số [4.6] Tool Encode V1 >>ON<<")
print("[</>] Nhập Số [4.7] Tool Encode V2 >>ON<<")
print("[</>] Nhập Số [00] THOÁT TOOL")

print("════════════════════════════════════════════════  ")
chon = str(input('[</>] Nhập Số \033[1;37m: '))