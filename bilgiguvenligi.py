import gmpy2
import time

# Çiftler (p, q) ve M
data = [
    [(23, 41, 99)],
    # diğer çiftleri de aynı formatta ekleyin
]

e = 1093  # genellikle RSA'da kullanılan standart e değeri

for pairs in data:
    for p, q, M in pairs:
        # Hesaplamalar
        N = p * q
        phi = (p - 1) * (q - 1)

        # Gizli Anahtar hesaplama
        start = time.time()
        d = gmpy2.invert(e, phi)
        D_time = time.time() - start

        # Şifreleme
        start = time.time()
        C = pow(M, e, N)
        encryption_time = time.time() - start

        # Deşifreleme
        start = time.time()
        M_decrypted = pow(C, d, N)
        decryption_time = time.time() - start

        print(f'p={p}, q={q}, M={M}')
        print(f'N={N}, phi={phi}, d={d}')
        print(f'Şifreleme süresi: {encryption_time} saniye')
        print(f'Şifreli metin: {C}')
        print(f'Gizli Anahtar Hesaplama Süresi (D Time): {D_time} saniye')
        print(f'Deşifreleme süresi: {decryption_time} saniye')
        print(f'Deşifrelenen metin: {M_decrypted}')
        print('-----------------------------')
