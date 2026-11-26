
(function () {
  document.querySelectorAll('.menu-toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var list = document.getElementById(btn.getAttribute('aria-controls'));
      var open = list.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
})();

(function () {
  var btn = document.getElementById('review-toggle');
  var wrap = document.getElementById('leave-review');
  if (!btn || !wrap) return;
  btn.addEventListener('click', function () {
    var open = wrap.hidden;
    wrap.hidden = !open;
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (open) { var f = document.getElementById('r-name'); if (f) f.focus(); }
  });
})();
function ppReviewCheck(form, status) {
  var rating = form.querySelector('input[name="rating"]:checked');
  if (!form.name.value.trim() || !form.review.value.trim() || !rating) {
    status.className = 'form-status error';
    status.textContent = 'Please add your name, a rating and your review.';
    return null;
  }
  if (!form.consent.checked) {
    status.className = 'form-status error';
    status.textContent = 'Please tick the box so we may display your review.';
    return null;
  }
  return rating.value;
}

(function () {
  var form = document.getElementById('contact-form');
  if (!form) return;
  var TO = 'info@propodiumevents.com';
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var status = document.getElementById('form-status');
    var name = form.name.value.trim(), email = form.email.value.trim();
    if (!name || !email || !form.email.checkValidity()) {
      status.className = 'form-status error';
      status.textContent = 'Please add your name and a valid email address.';
      return;
    }
    var svc = Array.prototype.slice.call(form.querySelectorAll('input[name="services"]:checked')).map(function (c) { return c.value; });
    var body = 'Name: ' + name + '\nCompany: ' + form.company.value + '\nEmail: ' + email + '\nPhone: ' + form.phone.value +
      '\nEvent and city: ' + form.event.value + '\nDates: ' + form.dates.value + '\nGuests: ' + form.guests.value + '\nAirport arrivals: ' + form.airport.value + '\nServices: ' + svc.join(', ') + '\n\n' + form.message.value;
    window.location.href = 'mailto:' + TO + '?subject=' + encodeURIComponent('Quote request from ' + name) + '&body=' + encodeURIComponent(body);
    status.className = 'form-status';
    status.textContent = 'Your email app should open with the message ready to send.';
  });
})();

(function () {
  var form = document.getElementById('review-form');
  if (!form) return;
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var status = document.getElementById('review-status');
    var rating = ppReviewCheck(form, status);
    if (!rating) return;
    var body = 'Name: ' + form.name.value.trim() + '\nCompany / Role: ' + form.role.value + '\nEvent: ' + form.event.value +
      '\nRating: ' + rating + ' of 5\nConsent to display on the website: yes\n\n' + form.review.value;
    window.location.href = 'mailto:info@propodiumevents.com?subject=' + encodeURIComponent('Website review from ' + form.name.value.trim()) + '&body=' + encodeURIComponent(body);
    status.className = 'form-status';
    status.textContent = 'Thank you! Your review will appear on our site once approved. Your email app opens with the review ready to send.';
  });
})();
