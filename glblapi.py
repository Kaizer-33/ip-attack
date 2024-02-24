import phonenumbers as pnumb
from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone


def sorgugl(numara):
    parsing = parse(numara)
    loc = geocoder.description_for_number(parsing, "id")
    isp = carrier.name_for_number(parsing, "id")
    tz = timezone.time_zones_for_number(parsing)

    print("\033[92mBilgi \033[0m:", parsing)
    print("\033[92mUluslararası format \033[0m:", pnumb.normalize_digits_only(parsing))
    print("\033[92mUlusal format \033[0m:", pnumb.national_significant_number(parsing))
    print("\033[92mNumara geçerli \033[0m:", pnumb.is_valid_number(parsing))
    print("\033[92mUluslararası iletişim kurulabilir \033[0m:", pnumb.can_be_internationally_dialled(parsing))
    print("\033[92mKonum \033[0m:", loc)
    print("\033[92mNumara alan kodu \033[0m:", pnumb.region_code_for_number(parsing))
    print("\033[92mNumara türü \033[0m:", pnumb.number_type(parsing))
    print("\033[92mBelirli bir operatör \033[0m:", pnumb.is_carrier_specific(parsing))
    print("\033[92mOperatör \033[0m:", isp)
    print("\033[92mSaat dilimi \033[0m:", tz)
    print("\033[92mCoğrafi numaraları içerir \033[0m:", pnumb.is_number_geographical(parsing))

if __name__ == "__main__":
    numara = input("Global No Sorgu İçin +90 Şeklinde Giriniz:")
    sorgugl(numara)
