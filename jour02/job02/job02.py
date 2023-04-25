import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from job01.job01 import Personne, Eleve, Professeur

if __name__ == "__main__":
    eleve_2 = Eleve()
    eleve_2.bonjour(), eleve_2.aller_en_cours()
    eleve_2.modifier_age(15)

    print()

    prof_2 = Professeur("")
    prof_2.modifier_age(40)
    prof_2.bonjour(), prof_2.enseigner()