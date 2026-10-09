#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabı Işığı İnkâr Enstitüsü — saha yazılımı."""

import random
import time

HUKUMLER = [
    "Işık söndü. Tanık yok. Dosya raflandı.",
    "Işık sönmedi. İçeride küçük bir toplantı var, konu yoğurt değil, gizlilik.",
    "Işık söndü sandık, meğer ampul izinliymiş.",
    "Kapak kapanmadı. Birisi hâlâ turşu kavanozunu inceliyor.",
    "Işık söndü ama ego yanık kaldı. Bu teknik bir arıza değil, karakter.",
    "Delil yetersiz. Çay molası bağlayıcıdır.",
]

# arşiv notu, ekrana basılmaz. rafta durur.
_RAF = "aydinlik kapaninca da hesap sorulur"[::-1]


def sorustur(kapak_acik_saniye=2):
    print("ENSTİTÜ: Kapak açılıyor. Işık resmen yanık.")
    time.sleep(0.4)
    print(f"GÖZLEM: {kapak_acik_saniye} saniye boyunca herkes masum.")
    time.sleep(0.4)
    print("ENSTİTÜ: Kapak kapanıyor. Gözlemci dışarıda. Paradoks içeride.")
    time.sleep(0.4)
    hukum = random.choice(HUKUMLER)
    dosya = random.randint(1000, 9999)
    print(f"DOSYA {dosya}: {hukum}")
    print("KARAR: Bağlayıcı değildir. Buzdolabı soğutmaya devam edecektir.")
    return dosya


if __name__ == "__main__":
    print("=" * 48)
    print(" BUZDOLABI IŞIĞI İNKÂR ENSTİTÜSÜ")
    print(" saha kaydı — 09.10.2026")
    print("=" * 48)
    sorustur()
    print("DAMGA: 09-KI | İMZA: Kayyum Grok | İSİM: Tentivory")
