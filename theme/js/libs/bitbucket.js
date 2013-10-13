/*
UI functions dedicated to the Bitbucket modal panel
*/

var bitbucket_api = 'https://api.bitbucket.org/1.0'
var bitbucket_endpoints = {}
var spinner = (new Spinner(spin_opts)).spin();
var template = null;
var url = null;
var bitbucket_data = {};

$('a[id^="Bitbucket-link"]').click(function (e)
{
    e.preventDefault();
    var url = prepare_link(e, this);
    adjustSelection("Bitbucket-link");
    remove_modal();
    showBitbucket(url, this);
});

function showBitbucket(e, t) {
    url = t.href;
    var bitbucket_profile = $("#bitbucket-profile");
    bitbucket_endpoints['user'] = bitbucket_api + '/users/' + bitbucket_username;
    bitbucket_endpoints['followers'] = bitbucket_endpoints['user'] + '/followers';
    bitbucket_endpoints['repositories'] = bitbucket_endpoints['user'] + '/repositories/' + bitbucket_username;
    if (bitbucket_profile.length > 0) {
        bitbucket_profile.modal('show');
    }
    else {
        $("#Bitbucket-link").append(spinner.el);

        $.get('/theme/templates/bitbucket-profile.html', function(data) {
            // Request succeeded, data contains HTML template, we can load data
            template = Handlebars.compile(data);

            try {
                $.ajax({
                    url: bitbucket_endpoints['user'],
                    dataType: "jsonp",
                    jsonpCallback: "readBitbucketData",
                    error: function(s, statusCode, errorThrown) {
                        window.location.href = url;
                        spinner.stop();
                    }
                });
            }
            catch (err) {
                window.location.href = url;
                spinner.stop();
            }
        })
        .error(function() {
            window.location.href = url;
            spinner.stop();
        });
    }
}

function readBitbucketData(user) {
    $.extend(bitbucket_data, user);
    $.ajax({
        url: bitbucket_endpoints['followers'],
        dataType: "jsonp",
        jsonpCallback: "readFollowers",
        error: function(s, statusCode, errorThrown) {
            window.location.href = url;
            spinner.stop();
        }
    });
}

function readFollowers(followers) {
    bitbucket_data['user']['followers'] = followers['count'];
    var html = template(bitbucket_data);
    $('body').append(html);
    $("#bitbucket-profile").modal();
    spinner.stop();
}
