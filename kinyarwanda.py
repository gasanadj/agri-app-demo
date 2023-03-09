import umuhinzi_type
import umuceri
import igisheke
import icyayi
import ibirayi
import ibishyimbo
import ibigori
import ibitoki
def kinyarwanda() :
        print("Ikaze kuri agri-app")
        print("Ubwoko bw umuhinzi")
        umuhinzi_type.umuhinzi()
        umuhinzi = int(input("Shiramo umubare uhuye n'ubwoko bw umuhinzi"))
        if (umuhinzi == 1):
            print("Wahisemo umuhinzi mugari")
            print("Hitamo igihingwa")
            print("1. Umuceri")
            print("2. Ibisheke")
            print("3. icyayi")
            igihingwa = int(input("Hitamo igihingwa :"))
            if (igihingwa == 1) :
                    umuceri.umuceri()
            elif (igihingwa == 2) :
                    igisheke.igisheke()
            elif (igihingwa == 3) :
                    icyayi.icyayi()
        elif (umuhinzi == 2):
            print("Wahisemo umuhinzi muto muto")
            print("Hitamo igihingwa cyawe")
            print("1. ibirayi")
            print("2. ibishyimbo")
            print("3. ibigori")
            print("4. ibitoki")
            igihingwa = int(input("Hitamo nimero ihuye n'igihingwa ushaka: "))
            if (igihingwa == 1):
                ibirayi.ibirayi()
            elif (igihingwa == 2):
                ibishyimbo.ibishyimbo()
            elif (igihingwa == 3):
                ibigori.ibigori()
            elif (igihingwa == 4):
                ibitoki.ibitoki() 
