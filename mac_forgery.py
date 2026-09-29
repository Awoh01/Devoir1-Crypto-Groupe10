"""
Partie 3.4 - Forgerie de MAC.

ATTENTION : la construction exacte de Mac_k(m) n'est donnee dans aucun
des documents de cours disponibles (voir explications/3_mac.md). Ce
fichier NE calcule PAS de tag final : il prepare la formule de
forgerie pour la seule construction "manuel de cours" plausible et
laisse le calcul final desactive tant que la construction n'est pas
confirmee.

Hypothese testee (a confirmer) : Mac_k(m) = troncature 32 bits de
(m XOR k), sur des messages/cles de 64 bits. Comme le XOR est
bit-a-bit, tronquer un XOR revient a faire le XOR des troncatures :

    tronc(A xor B) = tronc(A) xor tronc(B)

Donc si t_obs = tronc(m_obs xor k*), alors pour n'importe quel
m_cible :

    t_forge = t_obs xor tronc(m_obs xor m_cible)

sans jamais avoir besoin de connaitre k*. C'est exactement le type de
faiblesse (MAC "lineaire") illustre en cours a propos des constructions
a eviter.
"""

m_obs = 0x34de51e80a5b0373
t_obs = 0x4661f080
m_cible = 0xf330a664f8b1ecd2

MASK64 = (1 << 64) - 1
MASK32 = (1 << 32) - 1


def tronc_poids_faible(x64: int) -> int:
    return x64 & MASK32


def tronc_poids_fort(x64: int) -> int:
    return (x64 >> 32) & MASK32


def forger(hypothese_troncature):
    delta = (m_obs ^ m_cible) & MASK64
    t_forge = t_obs ^ hypothese_troncature(delta)
    return t_forge


if __name__ == '__main__':
    print("m_obs   =", hex(m_obs))
    print("t_obs   =", hex(t_obs))
    print("m_cible =", hex(m_cible))
    print()
    print("tag forge (poids faible) :", hex(forger(tronc_poids_faible)))
    print("tag forge (poids fort)   :", hex(forger(tronc_poids_fort)))
    print()
