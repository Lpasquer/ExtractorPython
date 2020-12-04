call echo "Se mettre dans le répertoire du projet Java"
cd VotreDisque:Votre\Répertoire\Du\Projet\Java

call echo "Installation"
mvn install

call echo "Compilation"
mvn compile

call echo "Installation terminée"
pause

call echo "Execution de l'extracteur Java"
call java -cp "target/WikipediaMatrix-1.0-SNAPSHOT.jar" pdl/wiki/WikipediaMatrix

call echo "Extraction terminée, veuillez lancer le deuxième script"