# Kâr Marjı ve KDV Hesaplayıcı
# Amaç: Bir ürünün alış ve satış fiyatından kâr, kâr marjı ve KDV'yi hesaplamak.

# --- Sabitler ---
GECERLI_KDV_ORANLARI = (1, 10, 20)   # Türkiye'deki KDV oranları (%)

print("=== Kâr Marjı ve KDV Hesaplayıcı ===")

# --- 1. Kullanıcıdan veri alma (input) ve tür dönüşümü ---
urun_adi = input("Ürün adı: ")                                   # str
alis_fiyati = float(input("Birim alış fiyatı (KDV hariç, TL): "))  # float
satis_fiyati = float(input("Birim satış fiyatı (KDV hariç, TL): "))  # float
adet = int(input("Satılan adet: "))                              # int
kdv_orani = int(input("KDV oranı (1, 10 veya 20): "))            # int

# --- 2. Girdi kontrolü (karşılaştırma operatörleri) ---
girdi_gecerli = (alis_fiyati >= 0 and satis_fiyati >= 0
                 and adet > 0 and kdv_orani in GECERLI_KDV_ORANLARI)  # bool

if not girdi_gecerli:
    print("Hatalı girdi: fiyatlar negatif, adet 0'dan küçük/eşit ya da KDV oranı geçersiz.")
else:
    # --- 3. Hesaplamalar (aritmetik operatörler) ---
    toplam_maliyet = alis_fiyati * adet            # toplam alış bedeli
    toplam_gelir = satis_fiyati * adet             # KDV hariç toplam satış
    kar = toplam_gelir - toplam_maliyet            # net kâr (zarar ise negatif)

    kdv_tutari = toplam_gelir * kdv_orani / 100    # satıştan doğan KDV
    kdv_dahil_toplam = toplam_gelir + kdv_tutari   # müşterinin ödeyeceği tutar

    # Kâr marjı = kâr / satış geliri * 100 (satış gelirine göre)
    if toplam_gelir > 0:
        kar_marji = kar / toplam_gelir * 100
    else:
        kar_marji = 0.0

    # --- 4. Biçimli çıktı (f-string) ---
    print(f"\n--- {urun_adi} için sonuçlar ---")
    print(f"Toplam maliyet      : {toplam_maliyet:,.2f} TL")
    print(f"Toplam gelir (KDV'siz): {toplam_gelir:,.2f} TL")
    print(f"Kâr / Zarar         : {kar:,.2f} TL")
    print(f"Kâr marjı           : %{kar_marji:.2f}")
    print(f"KDV tutarı (%{kdv_orani})   : {kdv_tutari:,.2f} TL")
    print(f"KDV dahil toplam    : {kdv_dahil_toplam:,.2f} TL")

    # --- 5. Karşılaştırma ile yorum ---
    if kar > 0:
        print("Durum: Kârdasınız.")
    elif kar == 0:
        print("Durum: Başa baş noktasındasınız.")
    else:
        print("Durum: Zarardasınız!")
