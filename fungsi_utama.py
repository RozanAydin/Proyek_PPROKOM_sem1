import os
from art import text2art
import fitur1
import fitur2
import fitur3
import fitur4

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def fungsi_utama():
    while True:
        print("-" * 69)
        print(text2art("KIDUNG    ASA", font="standard"))
        print("-" * 69)
        print("\n") 
        print("========== MENU ==========") 
        print("[1] Fitur 1")
        print("[2] Fitur 2")
        print("[3] Fitur 3")
        print("[4] Fitur 4")
        print("[5] Keluar")
        menu = (input("PILIH MENU> "))
        print("\n")

        if menu == "1":
            bersihkan_layar() 
            fitur1.menu_fitur1()
        elif menu == "2": 
            bersihkan_layar() 
            fitur2.menu_fitur2() 
        elif menu == "3": 
            bersihkan_layar() 
            fitur3.menu_fitur3()
        elif menu == "4":
            bersihkan_layar() 
            fitur4.menu_fitur4()
        elif menu == "5": 
            print("Terimakasih telah menggunakan program Kidung Asa")
            exit() 
        else: 
            bersihkan_layar() 
            print("Input Salah!")

fungsi_utama()