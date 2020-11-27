call echo "Execution des extracteurs Java (HTML puis Wikitext)"

call mvn compile -f "C:\Users\Admin\Documents\PDL\PDLProject-master"

call mvn package -f "C:\Users\Admin\Documents\PDL\PDLProject-master" 

cd "C:\Users\Admin\Documents\PDL\PDLProject-master"

call echo "Appel de l’extracteur Java HTML"

call java -cp "target/WikipediaMatrix-1.0-SNAPSHOT.jar" fr.istic.HTMLExtractor

call echo "Appel de l’extracteur Java Wikitext"

call java -cp target/WikipediaMatrix-1.0-SNAPSHOT.jar " fr.istic.WikiTextExtractor

