const form = document.getElementById("form")
form. addEventListener('submit', function (event) {
    event.preventDefault();

        const fullname = document.getElementById('fullname').value.trim();
        const email = document.getElementById('email').value.trim();
        const age = document.getElementById('age').value;
        const contact = document.getElementById('contact').value.trim();

        if (fullname == " "){
            alert ("Ingresa tu nombre y apellido")
            return
        }

        if (!fullname.includes (" ")) {
            alert ("Ingresa tu nombre y apellido")
            return
        }

        if (!email.includes ("@")) {
            alert ("Ingresa un mail valido")
            return
        }

        if (age < 18) {
            return
            alert ("Para contactarnos debe ser mayor de edad")
        }

        if (contact==""){
            return
            alert ("Por favor, detalle su motivo de contacto")
        }

        const Contacto = {
            name: fullname, 
            mail: email, 
            age: age, 
            explanation: contact
        }

        console. log (Contacto)

    })