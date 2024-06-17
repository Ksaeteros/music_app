#!/bin/bash

# Crear directorios para los informes
mkdir -p reports

# Calcular la complejidad ciclomática y guardar el resultado
radon cc client/ web/ server/ -a -j > reports/radon_report.json

# Ejecutar pruebas y calcular la cobertura
coverage run -m unittest discover tests
coverage html -d reports/coverage

# Crear index.html con resultados
cat << 'EOF' > reports/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test and Coverage Report</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Test and Coverage Report</h1>
        
        <h2 class="mt-4">Coverage Report</h2>
        <iframe src="coverage/index.html" width="100%" height="500"></iframe>
        
        <h2 class="mt-4">Cyclomatic Complexity Report</h2>
        <pre><code id="radon-report"></code></pre>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script>
        $.getJSON('radon_report.json', function(data) {
            var reportText = JSON.stringify(data, null, 2);
            $('#radon-report').text(reportText);
        });
    </script>
</body>
</html>
EOF

# Mover el archivo JSON a la carpeta reports para que sea accesible desde el navegador
mv reports/radon_report.json reports/

# Mostrar mensaje
echo "Report generated at reports/index.html"
