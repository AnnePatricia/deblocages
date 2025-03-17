let deblocageSvgEyeOn = document.getElementById("deblocage-svg-eye-on");
let deblocageSvgEyeOff = document.getElementById("deblocage-svg-eye-off");
let deblocagePassword = document.getElementById("deblocage-password");

if(deblocageSvgEyeOn){
    deblocageSvgEyeOn.addEventListener("click", () => {
        deblocageSvgEyeOn.classList.toggle("deblocage-none");
        deblocageSvgEyeOff.classList.toggle("deblocage-none");
        deblocagePassword.type = "text";
    });
    deblocageSvgEyeOff.addEventListener("click", () => {
        deblocageSvgEyeOff.classList.toggle("deblocage-none");
        deblocageSvgEyeOn.classList.toggle("deblocage-none");
        deblocagePassword.type = "password";
    });
}

/* ACCORDION */

let deblocageAccordionElt = document.querySelectorAll(".deblocage-accordion-elt");

if(deblocageAccordionElt){
    deblocageAccordionElt.forEach((elt) => {
        if(elt.classList.contains("deblocage-accordion-elt-active")){
            elt.querySelector(".deblocage-cacher-text").textContent = "Cacher";
        }else{
            elt.querySelector(".deblocage-cacher-text").textContent = "Afficher";
        }
        elt.querySelector(".deblocage-cacher-text").addEventListener("click", () => {
            elt.classList.toggle("deblocage-accordion-elt-active");
            if(elt.classList.contains("deblocage-accordion-elt-active")){
                elt.querySelector(".deblocage-cacher-text").textContent = "Cacher";
            }else{
                elt.querySelector(".deblocage-cacher-text").textContent = "Afficher";
            }
        });
    });
}
/* ACCORDION */

/* DEBLOCAGE SINGLE */

let deblocageBtnQuitter = document.getElementById("deblocage-btn-quitter");
let deblocageDemandeDePretsSingle = document.getElementById("deblocage-demande-de-prets-single");
let deblocageTableauPretsBody = document.querySelectorAll(".deblocage-tableau-prets-body");

deblocageTableauPretsBody.forEach((elt) => {
    elt.addEventListener("click", () => {
        deblocageDemandeDePretsSingle.classList.toggle("deblocage-none");
    });
});

if(deblocageBtnQuitter){
    deblocageBtnQuitter.addEventListener("click", () => {
        deblocageDemandeDePretsSingle.classList.toggle("deblocage-none");
    });
}

document.getElementById('save-button').addEventListener('click', function() {
    // Collecter les données du formulaire
    const clientNumber = document.getElementById('client-number').value;
    const loanAmount = document.getElementById('loan-amount').value;
    const siteVisitDate = document.getElementById('site-visit-date').value;
    const notaryStatement = document.getElementById('notary-statement').files[0];
    const handwrittenRequest = document.getElementById('handwritten-request').files[0];

    // Vérifier si la case est cochée
    const isChecked = document.getElementById('deblocage-checkbox').checked;

    if (!isChecked) {
        alert("Veuillez cocher la case pour valider la demande de déblocage.");
        return;
    }

    // Créer un objet avec les données
    const formData = {
        clientNumber,
        loanAmount,
        siteVisitDate,
        notaryStatement: notaryStatement ? notaryStatement.name : null,
        handwrittenRequest: handwrittenRequest ? handwrittenRequest.name : null
    };

    // Enregistrer les données (par exemple, dans le localStorage)
    localStorage.setItem('deblocageFormData', JSON.stringify(formData));

    // Afficher un message de succès
    alert("Les données ont été enregistrées avec succès !");

    // Optionnel: Envoyer les données à un serveur
    // fetch('/api/save', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json',
    //     },
    //     body: JSON.stringify(formData),
    // })
})
