"use strict";
var ktwizard1;

var KTWizard1 = function () {
    var e, r;
    return {
        init: function () {
            var i;
            KTUtil.get("kt_wizard_v1"), e = $("#kt_form"), (ktwizard1 = new KTWizard("kt_wizard_v1", {
                startStep: 1,
                clickableSteps: false
            })).on("beforeNext", function (e) {
                !0 !== r.form() && e.stop()

                // validate required fields here
                const steps = $('.kt-wizard-v1__content')

                if (ktwizard1.getStep() > steps.length) return

                const toValidate = $('.kt-wizard-v1__content:nth(' + (ktwizard1.getStep() - 1) + ')').find('input, select').filter('[required]').toArray()
                toValidate.forEach(function (item, index) {
                    if ($(item).attr('type') == "checkbox") {
                        if ($(item).is(":checked") == false) {
                            ktwizard1.stop()

                            KTUtil.scrollTop(), swal.fire({
                                title: "",
                                text: "Please check all required checkboxes.",
                                type: "error",
                                confirmButtonClass: "btn btn-secondary"
                            })
                        }
                    } else {
                        if ($(item).val() < 0 || $(item).val() == "") {
                            ktwizard1.stop()

                            KTUtil.scrollTop(), swal.fire({
                                title: "",
                                text: "Please fill all required fields.",
                                type: "error",
                                confirmButtonClass: "btn btn-secondary"
                            })
                        }
                    }
                })

                // fill this input value where required
                toValidate.forEach(function (item, index) {
                    const toFill = document.getElementById($(item).attr('name') + '_val')

                    if (toFill) {
                        if ($(item).prop('tagName') == 'SELECT')
                            toFill.innerText = $(item).find('option:selected').text()
                        else
                            toFill.innerText = $(item).val()
                    }
                })

                // check if any duplicate values exist (specific for admissions wizard)
                if ($('#items_table')) {
                    if (duplicatesExist()) {
                        ktwizard1.stop()

                        KTUtil.scrollTop(), swal.fire({
                            title: "",
                            text: "There are some duplicate entries in your selection. Please remove them.",
                            type: "error",
                            confirmButtonClass: "btn btn-secondary"
                        })
                    }
                }
            }), ktwizard1.on("beforePrev", function (e) {
                /*!0 !== r.form() && e.stop()*/
            }), ktwizard1.on("change", function (e) {
                setTimeout(function () {
                    KTUtil.scrollTop()
                }, 500)
            }), r = e.validate({
                ignore: ":hidden",
                rules: {
                    // degree: {
                    //     required: true
                    // },
                    // postcode: {
                    //     required: !0
                    // },
                },
                invalidHandler: function (e, r) {
                    // KTUtil.scrollTop(), swal.fire({
                    //     title: "",
                    //     text: "There are some errors in your submission. Please correct them.",
                    //     type: "error",
                    //     confirmButtonClass: "btn btn-secondary"
                    // })
                },
                submitHandler: function (e) { }
            }), (i = e.find('[data-ktwizard-type="action-submit"]')).on("click", function (ktwizard1) {
                console.log("wizard handler")
                ktwizard1.preventDefault(), r.form() && (KTApp.progress(i), e.ajaxSubmit({
                    success: function () {
                        KTApp.unprogress(i), swal.fire({
                            title: "",
                            text: "The application has been successfully submitted!",
                            type: "success",
                            confirmButtonClass: "btn btn-secondary"
                        })
                    }
                }))
            })
        }
    }
}();

function duplicatesExist() {
    const items = $('#item_table tbody tr')
    const priorities = items.find('.priority_unit').toArray().map(p => p.value)
    const programs = items.find('.program_unit').toArray().map(p => p.value)

    return (new Set(priorities)).size !== priorities.length || (new Set(programs)).size !== programs.length
}

$(document).ready(function () {
    KTWizard1.init()
});