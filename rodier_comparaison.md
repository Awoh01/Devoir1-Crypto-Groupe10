# Comparaison des résultats — Groupe 10

Auteur de la contribution : Rodier Marcel Tumamo Simo.
Paramètres : `Equipe_03.txt`. Les résultats ci-dessous ont été vérifiés par le script.
Les cases de relecture humaine restent ouvertes pour la comparaison du groupe.

## 1.1 César alterné

| Exécution | Clé | Cryptogramme | Nombre de candidats selon le lexique du script |
| --- | --- | --- | --- |
| 1 | (2, 20) | `eyecgmvfgggmuuiyefcctufyebkzhlgl` | 1 |
| 2 | (19, 0) | `vevixsmlxmxslazevltikawevhbfyrxr` | 1 |
| 3 | (20, 8) | `wmwqyantyuyamiamwtuqlixmwpcnzzyz` | 1 |

## 1.2 Substitution

- Trace 1 : `afamfynqfzfyyrvfaqrmgrofapmhhgfg`.
- Trace 2 : `oqogqtveqnqttiuqoeigbidqolgffbqb`.
- Trace 3 : `xkxhkseokukssjgkxojhijqkxyhcciki`.

Texte clair :

```text
depuisdessiecleslesgenerauxetlesdiplomatescherchentatransmettreleursordressansquelennemipuisseleslireunprotocoledechangedeclespermetadeuxpersonnesdeconvenirdunsecretcommunenparlantdevanttoutlemondeunordinateurquantiquesuffisammentpuissantpourraitcasserplusieurssystemesdechiffrementutilisesaujourdhuisurinternetleselevesontmarchejusquausommetdelacollinepourobserverlecoucherdusoleilsurtoutelaregion
```

Clé complète compatible : `ivbyachtjulwrkdozfgpesmxqn`.

Les correspondances de k, w et z avec L, M et N ne sont pas déterminées par le texte observé : six complétions sont compatibles.

## 2.1 Masque jetable

| Exécution | Clé hexadécimale | Cryptogramme hexadécimal |
| --- | --- | --- |
| 1 | `48f42f09be44cd985c7b8094f0be6f0c53b20f06` | `59f0ad43d567c4b15cbf9254783e0b1d83e0cb97` |
| 2 | `13f6b41cb7c47c2ea63f8fe5fd14be142b6b8df7` | `02f23656dce77507a6fb9d257594da05fb394966` |
| 3 | `06ae29c5adf5b760e64d019df68e1b89e953ed68` | `17aaab8fc6d6be49e689135d7e0e7f98390129f9` |

## 2.2 Réutilisation de clé

XOR : `3aa2ca740dcb90986418aa0e9faebeafe6d5096908ec47739cddc0000000`.

Position du mot connu dans m1 : 23 (indices à partir de 0).

```text
m1 = modifiezimmediatementleprotocoledesecuritexxxxxx
m2 = leserveurcentralredemarreradimancheaminuitxxxxxx
k  = f5289bcb08154b7fc6aaca0684ece215d8fde5f67e5184521147bbab9e5d
```

Les deux phrases ont six x de bourrage. Les deux rechiffrements sont exacts.

## 3. MAC

| Message | Tag | Message modifié avec le même tag, accepté |
| --- | --- | --- |
| `0000000000000000` | `3d00bd90` | `8000000000000000` |
| `8000000000000000` | `3d00bd90` | `0000000000000000` |
| `00000000ffffffff` | `c2ff426f` | `80000000ffffffff` |
| `aaaaaaaaaaaaaaaa` | `97aa173a` | `2aaaaaaaaaaaaaaa` |

Partie basse de la clé observée : `4c3af3f3`.
Tag forgé : `b48b1f21`.
Une paire observée suffit pour fabriquer le tag de n’importe quel message cible.

## Bonus Vigenère

Longueur : 7. Clé : `beejkqr`. IC moyen : 0.08053.

```text
lereseauelectriquedelaregionasubiunepanneimportanteapreslatempetedeverglasdumoisdernierunattaquantpatientpeutessayertouteslesclespossiblesmaislespacedesclesestparfoistropvastepourcelaleprogrammelitlefichierligneparlignecompteleslettresetafficheuntableaudesfrequencesalecranunesignaturenumeriquepermetdeprouverquunmessageprovientbiendesonauteuretquilnapasetemodifieencheminpourverifierlintegritedunmessageonajouteuncodedauthentificationcalculeapartirduneclesecrete
```

## Grille à compléter pendant la réunion

| Partie | Rodier | Blakoua Adja | Cheikh Ahmadou Tidiane Ly | Odounlami Lucien Gbessemehlan | Décision du groupe |
| --- | --- | --- | --- | --- | --- |
| 1.1 César | Calculs proposés | À comparer | À comparer | À comparer | À compléter |
| 1.2 Substitution | Calculs proposés | À comparer | À comparer | À comparer | À compléter |
| 2.1 OTP | Calculs proposés | À comparer | À comparer | À comparer | À compléter |
| 2.2 et 2.3 Réutilisation | Calculs proposés | À comparer | À comparer | À comparer | À compléter |
| 3. MAC | Calculs proposés | À comparer | À comparer | À comparer | À compléter |
| Bonus Vigenère | Calculs proposés | À comparer | À comparer | À comparer | À compléter |

## Divergences et corrections

Indiquer ici la question, la différence constatée, sa cause, la correction retenue
et la personne qui l’a vérifiée. Ne pas marquer une validation humaine avant qu’elle ait été faite.
