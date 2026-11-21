
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
  var form = document.getElementById('contact-form');
  if (!form) return;
  var TO = 'EMAIL_AQUI';
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
