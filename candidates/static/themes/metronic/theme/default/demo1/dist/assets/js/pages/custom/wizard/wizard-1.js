"use strict";
var ktwizard1;
var rules = [
    ["select[name=degree]"],
    ["input[name=verification_status]"]
]

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

                // verify rules here
                if (ktwizard1.getStep() > rules.length) return
                rules[ktwizard1.getStep() - 1].forEach(function (item, index) {
                    if ($(item).attr('type') == "checkbox") {
                        if ($(item).is(":checked") == false) {
                            ktwizard1.stop()
                        }
                    } else {
                        if ($(item).val() < 0 || $(item).val() == "") {
                            ktwizard1.stop()
                        }
                    }
                })
            }), ktwizard1.on("beforePrev", function (e) {
                !0 !== r.form() && e.stop()
            }), ktwizard1.on("change", function (e) {
                setTimeout(function () {
                    KTUtil.scrollTop()
                }, 500)

                // if ($('div[data-ktwizard-type="step"]:nth(1)').attr('data-ktwizard-state') == 'done') {
                //     $.get('/applied-status', {'set': 1}, function (response) {
                //         console.log("set isApplied to 1")
                //     })
                // }
            }), r = e.validate({
                ignore: ":hidden",
                rules: {
                    degree: {
                        required: true
                    },
                    postcode: {
                        required: !0
                    },
                    city: {
                        required: !0
                    },
                    state: {
                        required: !0
                    },
                    country: {
                        required: !0
                    },
                    package: {
                        required: !0
                    },
                    weight: {
                        required: !0
                    },
                    width: {
                        required: !0
                    },
                    height: {
                        required: !0
                    },
                    length: {
                        required: !0
                    },
                    delivery: {
                        required: !0
                    },
                    packaging: {
                        required: !0
                    },
                    preferreddelivery: {
                        required: !0
                    },
                    locaddress1: {
                        required: !0
                    },
                    locpostcode: {
                        required: !0
                    },
                    loccity: {
                        required: !0
                    },
                    locstate: {
                        required: !0
                    },
                    loccountry: {
                        required: !0
                    }
                },
                invalidHandler: function (e, r) {
                    KTUtil.scrollTop(), swal.fire({
                        title: "",
                        text: "There are some errors in your submission. Please correct them.",
                        type: "error",
                        confirmButtonClass: "btn btn-secondary"
                    })
                },
                submitHandler: function (e) { }
            })//, (i = e.find('[data-ktwizard-type="action-submit"]')).on("click", function (ktwizard1) {
            //      console.log("wizard handler")
            //      ktwizard1.preventDefault(), r.form() && (KTApp.progress(i), e.ajaxSubmit({
            //         success: function () {
            //             KTApp.unprogress(i), swal.fire({
            //                 title: "",
            //                 text: "The application has been successfully submitted!",
            //                 type: "success",
            //                 confirmButtonClass: "btn btn-secondary"
            //             })
            //         }
            //     }))
            // })
        }
    }
}();
jQuery(document).ready(function () {
    KTWizard1.init()
});