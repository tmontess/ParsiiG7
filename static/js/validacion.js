const form = document.getElementById("form");

if (form) {
    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const fullnameElement = document.getElementById('fullname');
        const emailElement = document.getElementById('email');
        const ageElement = document.getElementById('age');
        const contactElement = document.getElementById('contacto');

        if (fullnameElement && emailElement && ageElement && contactElement) {
            const fullname = fullnameElement.value.trim();
            const email = emailElement.value.trim();
            const age = ageElement.value;
            const contact = contactElement.value.trim();

            if (fullname === "") {
                alert("Ingresa tu nombre y apellido");
                return;
            }

            if (!fullname.includes(" ")) {
                alert("Ingresa tu nombre y apellido");
                return;
            }

            if (!email.includes("@")) {
                alert("Ingresa un correo válido");
                return;
            }

            if (age < 18) {
                alert("Para contactarnos debes ser mayor de edad");
                return;
            }

            if (contact === "") {
                alert("Por favor, detalla tu motivo de contacto");
                return;
            }

            // Si todas las validaciones pasan, puedes continuar con el envío del formulario.
            // Si deseas enviar los datos al servidor, puedes hacerlo aquí.

            const contacto = {
                name: fullname,
                mail: email,
                age: age,
                explanation: contact
            };

            console.log(contacto);
        }
    });
}
