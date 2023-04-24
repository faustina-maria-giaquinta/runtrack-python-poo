class Student:
    def __init__(self, prenom, nom, id_etudiant):
        self.__prenom = prenom
        self.__nom = nom
        self.__id_etudiant = id_etudiant
        self.__n_credits = 0

    def add_credits(self, credits_to_add):
        self.__n_credits += credits_to_add

    def _student_eval(self):
        status = ""
        if self.__n_credits >= 90:
            status = "Excellent"
        elif self.__n_credits >= 80:
            status = "Très bien"
        elif self.__n_credits >= 70:
            status = "Bien"
        elif self.__n_credits >= 60:
            status = "Passable"
        else:
            status = "Insuffisant"
        self._level = status
    
    def student_info(self):
        self._student_eval()
        print(f"Prénom = {self.__prenom}\nNom = {self.__nom}\nid = {self.__id_etudiant}\nNiveau = {self._level}")
        
    # end def


if __name__ == "__main__":
    student = Student("John", "Doe", 145)

    for _ in range(3):
        student.add_credits(10)

    print(f"Le nombre de credits de {student._Student__prenom} {student._Student__nom} est de {student._Student__n_credits} points", end="\n\n")

    for _ in range(4):
        student.add_credits(10)
    student.student_info()