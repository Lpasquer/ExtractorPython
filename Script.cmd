call echo "Se mettre dans le répertoire du projet Java"
cd C:\Users\Admin\Documents\GitHub\PDLProject

call echo "Installation"
mvn install

call echo "Compilation"
mvn compile

call echo "Execution de l'extracteur Java"
call java -cp "target/WikipediaMatrix-1.0-SNAPSHOT.jar" pdl/wiki/WikipediaMatrix

call echo "Se mettre dans le répertoire du projet python"
cd C:\Users\Admin\Documents\GitHub\ExtractorPython

call echo "Ouverture de l'extracteur python"
call extracteur.py


