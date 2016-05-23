/*contenido_textarea = "" 
num_caracteres_permitidos = 10 

function valida_longitud(){ 
   num_caracteres = document.forms[0].texto.value.length 

   if (num_caracteres > num_caracteres_permitidos){ 
      document.forms[0].texto.value = contenido_textarea 
   }else{ 
      contenido_textarea = document.forms[0].texto.value 
   } 

   if (num_caracteres >= num_caracteres_permitidos){ 
      document.forms[0].caracteres.style.color="#ff0000"; 
   }else{ 
      document.forms[0].caracteres.style.color="#000000"; 
   } 

   cuenta() 
} 
function cuenta(){ 
   document.forms[0].caracteres.value=document.forms[0].texto.value.length 
} */

function limita(elEvento, maximoCaracteres) {
  var elemento = document.getElementById("texto");
 
  // Obtener la tecla pulsada 
  var evento = elEvento || window.event;
  var codigoCaracter = evento.charCode || evento.keyCode;
  // Permitir utilizar las teclas con flecha horizontal
  if(codigoCaracter == 37 || codigoCaracter == 39) {
    return true;
  }
 
  // Permitir borrar con la tecla Backspace y con la tecla Supr.
  if(codigoCaracter == 8 || codigoCaracter == 46) {
    return true;
  }
  else if(elemento.value.length >= maximoCaracteres ) {
    return false;
  }
  else {
    return true;
  }
}
 function pegar()
 {
    var texto = document.getElementById('texto');
    document.getElementById('missatges').value = texto.value;

 }
function actualizaInfo(maximoCaracteres) {
  var elemento = document.getElementById("texto");
  var info = document.getElementById("info");
 
  if(elemento.value.length >= maximoCaracteres ) {
    info.innerHTML = "Máximo "+maximoCaracteres+" caracteres";
  }
  else {
    info.innerHTML = "Puedes escribir hasta "+(maximoCaracteres-elemento.value.length)+" caracteres adicionales";
  }
}