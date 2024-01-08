<?php
$nom_fichier_csv = 'resultats_spheres.csv';

if (($handle = fopen($nom_fichier_csv, 'r')) !== false) {
    echo '<table border="1">';
    
    $en_tete = fgetcsv($handle);
    echo '<tr>';
    foreach ($en_tete as $colonne) {
        echo '<th>' . htmlspecialchars($colonne) . '</th>';
    }
    echo '</tr>';
    
    // Lire les données du fichier CSV
    while (($ligne = fgetcsv($handle)) !== false) {
        echo '<tr>';
        foreach ($ligne as $valeur) {
            echo '<td>' . htmlspecialchars($valeur) . '</td>';
        }
        echo '</tr>';
    }
    
    echo '</table>';
    
    fclose($handle);
} else {
    echo 'Erreur lors de l\'ouverture du fichier CSV.';
}
?>
