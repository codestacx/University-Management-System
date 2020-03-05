"use strict";
const AdmissionsXDropzone = {
    init: function () {
        $("#kt_dropzone_1").dropzone({
            url: "https://keenthemes.com/scripts/void.php",
            paramName: "file",
            maxFiles: 1,
            maxFilesize: 5,
            addRemoveLinks: !0,
            accept: function (e, o) {
                "justinbieber.jpg" == e.name ? o("Naha, you don't.") : o()
            }
        }), $("#kt_dropzone_2").dropzone({
            url: "https://keenthemes.com/scripts/void.php",
            paramName: "file",
            maxFiles: 10,
            maxFilesize: 10,
            addRemoveLinks: !0,
            accept: function (e, o) {
                "justinbieber.jpg" == e.name ? o("Naha, you don't.") : o()
            }
        }), $("#paid_challan_entrytest_dropzone").dropzone({
            url: "/entry-test-application",
            paramName: "paid-challan-copy",
            headers: {
                'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()
            },
            maxFiles: 10,
            maxFilesize: 10,
            addRemoveLinks: !0,
            acceptedFiles: "image/*,application/pdf,.psd",
            autoProcessQueue: false,
            accept: function (e, o) {
                "justinbieber.jpg" == e.name ? o("Naha, you don't.") : o()
            },
            init: function() {
                const dzClosure = this; // Makes sure that 'this' is understood inside the functions below.
                console.log("dz init getting called")
                // for Dropzone to process the queue (instead of default form behavior):
                document.querySelector("button[data-ktwizard-type='action-submit']").addEventListener("click", function(e) {
                    // Make sure that the form isn't actually being sent.
                    e.preventDefault();
                    e.stopPropagation();
                    console.log("dz handler")
                    dzClosure.processQueue();
                });
        
                //send all the form data along with the files:
                this.on("sending", function(data, xhr, formData) {
                    console.log("sending ...")
                    formData.append("degree", jQuery("select[name='degree']").val());
                    formData.append("verification_status", jQuery("input[name='verification_status']").val());
                    
                    window.location.href = '/'
                });
            }
        }),
            function () {
                var e = "#kt_dropzone_4",
                    o = $(e + " .dropzone-item");
                o.id = "";
                var n = o.parent(".dropzone-items").html();
                o.remove();
                var t = new Dropzone(e, {
                    url: "https://keenthemes.com/scripts/void.php",
                    parallelUploads: 20,
                    previewTemplate: n,
                    maxFilesize: 1,
                    autoQueue: !1,
                    previewsContainer: e + " .dropzone-items",
                    clickable: e + " .dropzone-select"
                });
                t.on("addedfile", function (o) {
                    o.previewElement.querySelector(e + " .dropzone-start").onclick = function () {
                        t.enqueueFile(o)
                    }, $(document).find(e + " .dropzone-item").css("display", ""), $(e + " .dropzone-upload, " + e + " .dropzone-remove-all").css("display", "inline-block")
                }), t.on("totaluploadprogress", function (o) {
                    $(this).find(e + " .progress-bar").css("width", o + "%")
                }), t.on("sending", function (o) {
                    $(e + " .progress-bar").css("opacity", "1"), o.previewElement.querySelector(e + " .dropzone-start").setAttribute("disabled", "disabled")
                }), t.on("complete", function (e) {
                    setTimeout(function () {
                        $("#kt_dropzone_4 .dz-complete .progress-bar, #kt_dropzone_4 .dz-complete .progress, #kt_dropzone_4 .dz-complete .dropzone-start").css("opacity", "0")
                    }, 300)
                }), document.querySelector(e + " .dropzone-upload").onclick = function () {
                    t.enqueueFiles(t.getFilesWithStatus(Dropzone.ADDED))
                }, document.querySelector(e + " .dropzone-remove-all").onclick = function () {
                    $(e + " .dropzone-upload, " + e + " .dropzone-remove-all").css("display", "none"), t.removeAllFiles(!0)
                }, t.on("queuecomplete", function (o) {
                    $(e + " .dropzone-upload").css("display", "none")
                }), t.on("removedfile", function (o) {
                    t.files.length < 1 && $(e + " .dropzone-upload, " + e + " .dropzone-remove-all").css("display", "none")
                })
            }(),
            function () {
                var e = "#kt_dropzone_5",
                    o = $(e + " .dropzone-item");
                o.id = "";
                var n = o.parent(".dropzone-items").html();
                o.remove();
                var t = new Dropzone(e, {
                    url: "https://keenthemes.com/scripts/void.php",
                    parallelUploads: 20,
                    maxFilesize: 1,
                    previewTemplate: n,
                    previewsContainer: e + " .dropzone-items",
                    clickable: e + " .dropzone-select"
                });
                t.on("addedfile", function (o) {
                    $(document).find(e + " .dropzone-item").css("display", "")
                }), t.on("totaluploadprogress", function (o) {
                    $(e + " .progress-bar").css("width", o + "%")
                }), t.on("sending", function (o) {
                    $(e + " .progress-bar").css("opacity", "1")
                }), t.on("complete", function (e) {
                    setTimeout(function () {
                        $("#kt_dropzone_5 .dz-complete .progress-bar, #kt_dropzone_5 .dz-complete .progress").css("opacity", "0")
                    }, 300)
                })
            }()
    }
};

KTUtil.ready(function () {
    AdmissionsXDropzone.init()
});