from automovil import Automovil
from camioneta_carga import CamionetaCarga

auto = Automovil("Mazda 3", "Rojo", "2.0", 4, 5, "Gasolina")
camioneta = CamionetaCarga("Chevrolet NHR", "Blanco", "3.0", 2, 3, "Diésel", 3500)

print(auto.arranque())
print(auto.climatizacion())
print(camioneta.info_extra())
