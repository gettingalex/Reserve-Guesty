

jQuery(function($){
        $.datepicker.regional['fr'] = {
          closeText: 'Fermer',
          prevText: '&#x3c;Préc. ',
          nextText: 'Suiv&#x3e;',
          currentText: 'Aujourd\'hui',
          monthNames: ['Janvier','F&#233;vrier','Mars','Avril','Mai','Juin',
          'Juillet','Ao&#251;t','Septembre','Octobre','Novembre','D&#233;cembre'],
          monthNamesShort: ['Jan','Fev','Mar','Avr','Mai','Jun',
          'Jul','Aou','Sep','Oct','Nov','Dec'],
          dayNames: ['Dimanche','Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi'],
          dayNamesShort: ['Dim','Lun','Mar','Mer','Jeu','Ven','Sam'],
          dayNamesMin: ['Di','Lu','Ma','Me','Je','Ve','Sa'],
          weekHeader: 'Sm',
          dateFormat: 'yy-mm-dd',
          firstDay: 1,
          isRTL: false,
          showMonthAfterYear: false,
          yearSuffix: '',
          minDate: 0,
          maxDate: '+12M +0D',
          numberOfMonths: 1,
          showButtonPanel: false,
          buttonImageOnly: true
          };
        $.datepicker.setDefaults($.datepicker.regional['fr']);
});
$(function(){
  $("#datepicker").datepicker();
});
$(function(){
  $("#datepicker2").datepicker();
});