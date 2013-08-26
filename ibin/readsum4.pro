function readsum4, sumf, file

   print, 'readsum4 input file : ', file

	openr, lun, file, /get_lun, error=ioerr
	if( ioerr ne 0 ) then begin
		printf, -2, !err_string
		return, 1
	endif

   openr, lun, file, /get_lun

   buf = ''
   dum = 0
	readf, lun, buf
	subs = strsplit( buf, /extract, count=count )
	ver = subs(0)
	tag = subs(1)
   ttl = subs(2:count-1)

   buf = ''
   readf, lun, buf
   readf, lun, nfit
   spechead = strarr(nfit)
   for i=0, nfit-1 do begin
      buf = ''
      readf, lun, buf
      spechead[i] = buf
   endfor

   buf = ''
   readf, lun, buf
   readf, lun, nret
   readf, lun, buf
   sret = strarr(nret)
   for i=0, nret-1 do begin
      buf = ''
      readf, lun, buf
      sret[i] = buf
   endfor

   buf = ''
   readf, lun, buf
   readf, lun, nband
   readf, lun, buf
   ;print, buf
   sband = strarr(nband)
   sjscn = strarr(nband)
   nscnb = intarr(nband)
   npts = intarr(nband)
   wstrt = fltarr(nband)
   wstop = fltarr(nband)
   nspac = fltarr(nband)
   for i=0, nband-1 do begin
      buf = ''
      readf, lun, buf
      sband[i] = buf
      ;print, sband[i]
      subs = strsplit( sband[i], /extract, count=count )
      nscnb[i] = subs[count-1] + 0
      ;print, count
      ;print, subs
      npts[i]     = subs[4] + 0
      wstrt[i]    = subs[1] + 0.0D0
      wstop[i]    = subs[2] + 0.0D0
      nspac[i]     = subs[3] + 0.0D0
      for j=0, nscnb[i]-1 do readf, lun, buf
   endfor

   readf, lun, buf
   readf, lun, buf
   parms = ''
   readf, lun, parms

   sumf = {                $
      ver  : ver,          $
      tag  : tag,          $
      ttl  : ttl,          $
      nfit : nfit,         $
      nret : nret,         $
      nbnd : nband,        $
      nscn : nscnb,        $
      npts : npts,        $
      wstr : wstrt,        $
      wstp : wstop,        $
      nspac : nspac, $
      shead : spechead,		$
		sret : sret,			$
		sbnd : sband,			$
		parms : parms	      $
		}

   free_lun, lun
   return, 0

stop
end