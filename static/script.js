$(function() {
  $('#navbar.navbar-right ul li a').click(function() {
    //clear active status of any parent LI's
    $('#navbar.navbar-right ul li').removeClass('active');

    // store id of new active sub-nav
    var currSub = $(this).parent();
    currSub.addClass('active');
    var id = currSub.attr('id');

    // clear active status of any sub-nav list
    $('#subnavbar ul.navbar-nav').removeClass('active');

    // set selected sub-nav to active
    $('.' + id).addClass('active');

    console.log($('.' + id).attr('class'));

  });

});


$("#input-ficons-5").fileinput({
  uploadUrl: "/file-upload-batch/2",
  uploadAsync: false,
  previewFileIcon: '<i class="fa fa-file"></i>',
  preferIconicPreview: true, // this will force thumbnails to display icons for following file extensions
  previewFileIconSettings: {
    // configure your icon file extensions
    mov: '<i class="far fa-file-video text-warning"></i>',
    mp3: '<i class="far fa-file-audio text-warning"></i>',
    img: '<i class="far fa-file-image text-danger"></i>',
    model: '<i class="fas fa-draw-polygon"></i>',
  },
  previewFileExtSettings: {
    // configure the logic for determining icon file extensions
    mov: function(ext) {
      return ext.match(/(avi|mpg|mkv|mov|mp4|3gp|webm|wmv)$/i);
    },
    mp3: function(ext) {
      return ext.match(/(mp3|wav)$/i);
    },
    img: function(ext) {
      return ext.match(/(jpg|gif|png|svg)$/i)
    },
    model: function(ext) {
      return ext.match(/(obj|fbx)$/i)
    }
  }
});