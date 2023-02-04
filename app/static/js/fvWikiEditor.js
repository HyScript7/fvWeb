var editor = new Quill("#editor", {
  modules: { toolbar: "#toolbar" },
  theme: "snow",
});

$(document).ready(function () {
  $("#editor-controls").on("submit", function () {
    var hvalue = $(".ql-editor").html();
    hvalue = hvalue.replace(/></g, ">\n<");
    $(this).append(
      "<textarea name='content' style='display:none'>" + hvalue + "</textarea>"
    );
  });
  // reset
  $("#editor-controls").on("reset", function () {
    editor.setContents([{ insert: "\n" }]);
  });
});
