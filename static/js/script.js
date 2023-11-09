document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById("form");

    if (form) {
        form.addEventListener('submit', async function (event) {
            event.preventDefault();

            const formData = new FormData(form);

            try {
                const response = await fetch('/api/forms-contacto', {
                    method: 'POST',
                    body: formData
                });

                if (response.ok) {
                    // La solicitud fue exitosa, muestra un mensaje de éxito
                    console.log('¡Éxito!');
                } else {
                    // La solicitud falló, muestra un mensaje de error
                    console.error('Error en la solicitud');
                }
            } catch (error) {
                console.error('Error en la solicitud:', error);
            }
        });
    }
});