Objectif:

créer un capteur de distance et de vitesse afin que le véhicule puisse se localiser dans l'espace. 
Dans cette démo la webcam de mon ordinateur est utilisée et le capteur de vitesse n'est pas implémenté, 
mais il suffirait de diviser la distance par des incréments de temps afin d'obtenir un capteur de vitesse.


fonctionnement:

À l'aide d'open cv (python) on applique on transforme le code de couleur de l'image qui est par défaut rgb en code de couleur hsv.
On définit une plage de couleur de rouge pour l’étalonnage de la couleur du laser. 
Ensuite on applique deux masques sur l'image un premier avec le rouge avec un angle positif dans le code de couleur hsv et 
un autre avec le rouge avec un angle négatif avec ce code de couleur.Avec cela ont créé une image booléenne (fenêtre mask) 
qui identifie en blanc les pixels dans l'image qui sont dans la plage de rouge définie. 
Après une multiplication matricielle est effectuée avec l'image initiale afin d'avoir les vraies couleurs de l'image (fenêtre res).
La mesure de distance est effectuée en calculant la distance entre le centre de l'image (point bleu) et le centroide du laser (point rouge). Afin d'éviter une pollution des données dues au rouge dans l'environnement le programme considère que le rouge dans la zone délimitée dans le carré vert pour sont calcul de distance.En étalonnant le capteur, on peut déterminer le nombre de radians par pixel de la caméra et sachant la distance entre le laser et la caméra et à l'aide d'un simple rapport trigonométrique (D = h/tan(thêta))  on obtient la distance entre le laser et la caméra.


projet:

https://github.com/featTheB/client_pgU1/blob/master/pgU1_client/video_processing/videoProcessing.py

référence :
 
https://sites.google.com/site/todddanko/home/webcam_laser_ranger
