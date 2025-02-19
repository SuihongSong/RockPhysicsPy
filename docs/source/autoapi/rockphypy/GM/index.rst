:py:mod:`rockphypy.GM`
======================

.. py:module:: rockphypy.GM


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   rockphypy.GM.GM




.. py:class:: GM

   
   Contact based granular medium models and extensions.
















   ..
       !! processed by numpydoc !!
   .. py:method:: ThomasStieber(phi_sand, phi_sh, vsh)
      :staticmethod:

      
      Thomas-Stieber porosity model for sand-shale system.

      :param phi_sand: clean sand porosity
      :type phi_sand: float
      :param phi_sh: shale porosity
      :type phi_sh: float
      :param vsh: volume faction of shale in the mixture
      :type vsh: float or array-like

      :returns: *float or array-like* -- phi_ABC,phi_AC (frac): porosity line as shown in Fig 5.3.2 in (Mavko,2020)















      ..
          !! processed by numpydoc !!

   .. py:method:: silty_shale(C, Kq, Gq, Ksh, Gsh)
      :staticmethod:

      
      Dvorkin–Gutierrez silty shale model: model the elastic moduli of decreasing clay content for shale.

      :param C: volume fraction of clay
      :type C: float or array-like
      :param Kq: bulk modulus of silt grains
      :type Kq: float
      :param Gq: shear modulus of silt grains
      :type Gq: float
      :param Ksh: saturated bulk modulus of pure shale
      :type Ksh: float
      :param Gsh: saturated shear modulus of pure shale, * Ksh and Gsh could be derived from well-log measurements of VP, VS and density in a pure shale zone.
      :type Gsh: float

      :returns: *float or array-like* -- K_sat, G_sat: elastic moduli of the saturated silty shale.















      ..
          !! processed by numpydoc !!

   .. py:method:: shaly_sand(phis, C, Kss, Gss, Kcc, Gcc)
      :staticmethod:

      
      Modeling elastic moduli for sand with increasing clay content using LHS bound rather than using Gassmann relation.

      :param phis: critical porosity of sand composite
      :type phis: float
      :param C: clay content
      :type C: float or array-like
      :param Kss: saturated bulk moduli for clean sandstone using e.g. HM
      :type Kss: float
      :param Gss: saturated shear moduli for clean sandstone using e.g. HM
      :type Gss: float
      :param Kcc: saturated bulk moduli calculated from the sandy shale model at critical clay content using silty shale model
      :type Kcc: float
      :param Gcc: saturated shear moduli calculated from the sandy shale model at critical clay content using silty shale model
      :type Gcc: float

      :returns: *float or array-like* -- K_sat,G_sat: saturated rock moduli of the shaly sand















      ..
          !! processed by numpydoc !!

   .. py:method:: contactcement(K0, G0, Kc, Gc, phi, phic, Cn, scheme)
      :staticmethod:

      
      Compute dry elastic moduli of cemented sandstone via Contact cement model by Dvorkin &Nur (1996).

      :param K0: Bulk modulus of grain material in GPa
      :type K0: float
      :param G0: Shear modulus of grain material in GPa
      :type G0: float
      :param Kc: Bulk modulus of cement
      :type Kc: float
      :param Gc: Shear modulus of cement
      :type Gc: float
      :param phi: Porosity
      :type phi: float or array-like
      :param phic: Critical Porosity
      :type phic: float
      :param Cn: coordination number
      :type Cn: float
      :param scheme:
                     Scheme of cement deposition
                             1=cement deposited at grain contacts
                             2=cement deposited at grain surfaces
      :type scheme: int

      :returns: *_type_* -- K_dry, G_dry (GPa): Effective elastic moduli of dry rock

      .. rubric:: References

      - Dvorkin & Nur, 1996, Geophysics, 61, 1363-1370















      ..
          !! processed by numpydoc !!

   .. py:method:: hertzmindlin(K0, G0, phic, Cn, sigma, f)
      :staticmethod:

      
      Compute effective dry elastic moduli of granular packing under hydrostatic pressure condition via Hertz-Mindlin approach. Reduced shear factor that honours the non-uniform contacts in the granular media is implemented.

      :param K0: Bulk modulus of grain material in GPa
      :type K0: float
      :param G0: Shear modulus of grain material in GPa
                 phic : float
                 Critical Porosity
      :type G0: float
      :param Cn: coordination number
      :type Cn: float
      :param sigma: effective stress
      :type sigma: float or array-like
      :param f: reduced shear factor between 0 and 1
                0=dry pack with inifinitely rough spheres;
                1=dry pack with infinitely smooth spheres
      :type f: float

      :returns: * **K_dry, G_dry** (*float or array-like*) -- effective elastic moduli of dry pack
                * *References* -- ----------
                * *- Rock physics handbook section 5.5.*
                * *- Bachrach, R. and Avseth, P. (2008) Geophysics, 73(6), E197–E209.*















      ..
          !! processed by numpydoc !!

   .. py:method:: softsand(K0, G0, phi, phic, Cn, sigma, f)
      :staticmethod:

      
      Soft-sand (unconsolidated sand) model: model the porosity-sorting effects using the lower Hashin-Shtrikman-Walpole bound. (Also referred to as the 'friable-sand model' in Avseth et al. (2010).

      :param K0: Bulk modulus of grain material in GPa
      :type K0: float
      :param G0: Shear modulus of grain material in GPa
      :type G0: float
      :param phi: Porosity
                  phic : float
                  Critical Porosity
      :type phi: float or array like
      :param Cn: coordination number
      :type Cn: float
      :param sigma: effective stress
      :type sigma: float or array-like
      :param f: reduced shear factor between 0 and 1
                0=dry pack with inifinitely rough spheres;
                1=dry pack with infinitely smooth spheres
      :type f: float

      :returns: * *float or array-like* -- K_dry, G_dry (GPa): Effective elastic moduli of dry pack
                * *References* -- ----------
                * *- The Uncemented (Soft) Sand Model in Rock physics handbook section 5.5*
                * *- Avseth, P.; Mukerji, T. & Mavko, G. Cambridge university press, 2010*















      ..
          !! processed by numpydoc !!

   .. py:method:: Walton(K0, G0, phic, Cn, sigma, f)
      :staticmethod:

      
      Compute dry rock elastic moduli of sphere packs based on the Walton (1987)' thoery. Reduced shear factor that honours the non-uniform contacts in the granular media is implemented.

      :param K0: Bulk modulus of grain material in GPa
      :type K0: float
      :param G0: Shear modulus of grain material in GPa
                 phic : float
                 Critical Porosity
      :type G0: float
      :param Cn: coordination number
      :type Cn: float
      :param sigma: effective stress
      :type sigma: float or array-like
      :param f: reduced shear factor between 0 and 1
                0=dry pack with inifinitely rough spheres;
                1=dry pack with infinitely smooth spheres
      :type f: float

      :returns: * *float or array-like* -- K_w, G_w: Effective elastic moduli of dry pack
                * *References* -- ----------
                * *- Walton model in Rock physics handbook section 5.5*
                * *- Walton, K., 1987, J. Mech. Phys. Solids, vol.35, p213-226.*
                * *- Bachrach, R. and Avseth, P. (2008) Geophysics, 73(6), E197–E209*















      ..
          !! processed by numpydoc !!

   .. py:method:: johnson(K0, G0, n, phi, epsilon, epsilon_axial, path='together')
      :staticmethod:

      
      effective theory for stress-induced anisotropy in sphere packs. The transversely isotropic strain is considered as a combination of hydrostatic strain and uniaxial strain.

      :param K0: Bulk modulus of grain material in GPa
      :type K0: float
      :param G0: Shear modulus of grain material in GPa
      :type G0: float
      :param n: coordination number
      :type n: float
      :param phi: porosity
      :type phi: float or array like
      :param epsilon: hydrostatic strain (negative in compression)
      :type epsilon: float or array like
      :param epsilon_axial: uniaxial strain (along 3-axis)
      :type epsilon_axial: float or array like
      :param path: 'together': the hydrostatic and uniaxial strains are applied simultaneously
                   'uni_iso': the uniaxial strain is applied first followed by a hydrostatic strain
                   'iso_uni': the hydrostatic strain is applied first followed by a uniaxial strain by default 'together'
      :type path: str, optional

      :returns: * *array and float* -- C: (matrix): VTI stiffness matrix
                  sigma33: non zero stress tensor component
                  sigma11: non zero stress tensor component, sigma11=sigma22
                * *References* -- ----------
                * *- Norris, A. N., and Johnson, D. L., 1997, ASME Journal of Applied Mechanics, 64, 39-49.*
                * *- Johnson, D.L., Schwartz, L.M., Elata, D., et al., 1998. Transactions ASME, 65, 380–388.*















      ..
          !! processed by numpydoc !!

   .. py:method:: stiffsand(K0, G0, phi, phic, Cn, sigma, f)
      :staticmethod:

      
      Stiff-sand model:  Modified Hashin-Shtrikman upper bound with Hertz-Mindlin end point, counterpart to soft sand model.
      model the porosity-sorting effects using the lower Hashin–Shtrikman–Walpole bound.

      :param K0: Bulk modulus of grain material in GPa
      :type K0: float
      :param G0: Shear modulus of grain material in GPa
      :type G0: float
      :param phi: Porosity
                  phic : float
                  Critical Porosity
      :type phi: float or array like
      :param Cn: coordination number
      :type Cn: float
      :param sigma: effective stress
      :type sigma: float or array-like
      :param f: reduced shear factor between 0 and 1
                0=dry pack with inifinitely rough spheres;
                1=dry pack with infinitely smooth spheres
      :type f: float

      :returns: *float or array-like* -- K_dry, G_dry (GPa): Effective elastic moduli of dry pack















      ..
          !! processed by numpydoc !!

   .. py:method:: constantcement(phi_b, K0, G0, Kc, Gc, phi, phic, Cn, scheme)
      :staticmethod:

      
      Constant cement (constant depth) model according to Avseth (2000)

      :param phi_b: adjusted high porosity end memeber
      :type phi_b: _type_
      :param K0: Bulk modulus of grain material in GPa
      :type K0: float
      :param G0: Shear modulus of grain material in GPa
      :type G0: float
      :param Kc: Bulk modulus of cement
      :type Kc: float
      :param Gc: Shear modulus of cement
      :type Gc: float
      :param phi: Porosity
      :type phi: float or array-like
      :param phic: Critical Porosity
      :type phic: float
      :param Cn: coordination number
      :type Cn: float
      :param scheme:
                     Scheme of cement deposition
                             1=cement deposited at grain contacts
                             2=cement deposited at grain surfaces
      :type scheme: int

      :returns: * *float or array-like* -- K_dry, G_dry (GPa): Effective elastic moduli of dry rock
                * *References* -- ----------
                * *- Avseth, P.; Dvorkin, J.; Mavko, G. & Rykkje, J. Geophysical Research Letters, Wiley Online Library, 2000, 27, 2761-2764*















      ..
          !! processed by numpydoc !!

   .. py:method:: MUHS(K0, G0, Kc, Gc, phi, phi_b, phic, Cn, scheme)
      :staticmethod:

      
      Increasing cement model: Modified Hashin-Strikmann upper bound blend with contact cement model. For elastically stiff sandstone modelling.

      :param K0: Bulk modulus of grain material in GPa
      :type K0: float
      :param G0: Shear modulus of grain material in GPa
      :type G0: float
      :param Kc: Bulk modulus of cement
      :type Kc: float
      :param Gc: Shear modulus of cement
      :type Gc: float
      :param phi: Porosity
      :type phi: float or array-like
      :param phi_b: adjusted high porosity end memeber
      :type phi_b: _type_
      :param phic: Critical Porosity
      :type phic: float
      :param Cn: coordination number
      :type Cn: float
      :param scheme:
                     Scheme of cement deposition
                             1=cement deposited at grain contacts
                             2=cement deposited at grain surfaces
      :type scheme: int

      :returns: * *float or array-like* -- K_dry, G_dry (GPa): Effective elastic moduli of dry rock
                * *References* -- ----------
                * *- Avseth, P.; Mukerji, T. & Mavko, G. Cambridge university press, 2010*















      ..
          !! processed by numpydoc !!

   .. py:method:: Digby(K0, G0, phi, Cn, sigma, a_R)
      :staticmethod:

      
      Compute Keff and Geff using Digby's model

      :param K0: Bulk modulus of grain material in GPa
      :type K0: float
      :param G0: Shear modulus of grain material in GPa
      :type G0: float
      :param phi: Porosity
      :type phi: float
      :param Cn: coordination number
      :type Cn: float
      :param sigma: stress
      :type sigma: float or array-like
      :param a_R: a_R (unitless): ratio of the radius of the initially bonded area to the grain radius
      :type a_R: float

      :returns: * *float or array-like* -- Keff, Geff (Gpa): effective medium stiffness
                * *References* -- ----------
                * *- Digby, P.J., 1981. Journal of Applied Mechanics, 48, 803–808.*















      ..
          !! processed by numpydoc !!

   .. py:method:: pcm(f, sigma, K0, G0, phi, phic, v_cem, v_ci, Kc, Gc, Cn, mode, scheme, f_)
      :staticmethod:

      
      Computes effective elastic moduli of patchy cemented sandstone according to Avseth (2016).

      :param f: volume fraction of cemented rock in the binary mixture
      :type f: float
      :param sigma: effective stress
      :type sigma: float or array-like
      :param K0: Bulk modulus of grain material in GPa
      :type K0: float
      :param G0: Shear modulus of grain material in GPa
      :type G0: float
      :param phi: Porosity
      :type phi: float
      :param phic: Critical Porosity
      :type phic: float
      :param v_cem: cement fraction in contact cement model. phi_cem= phic-vcem
      :type v_cem: float
      :param v_ci: cement threshold above which increasing cement model is applied
      :type v_ci: float
      :param Kc: bulk modulus of cement
      :type Kc: float
      :param Gc: shear modulus of cement
      :type Gc: float
      :param Cn: coordination number
      :type Cn: float
      :param mode: 'stiff' or 'soft'. stiffest mixing or softest mixing. Defaults to 'stiff'.
      :type mode: str
      :param scheme: contact cement scheme.
                     1=cement deposited at grain contacts
                     2=cement deposited at grain surfaces
      :type scheme: int
      :param f_: slip factor in HM modelling. Defaults to 0.5.
      :type f_: float

      .. note:: (Avseth,2016): If 10% is chosen as the “critical” cement limit, the  increasing cement model can be used in addition to the contact cement model. (Torset, 2020): with the increasing cement model appended at 4% cement"

      :returns: * *float or array-like* -- K_DRY, G_DRY (GPa): effective elastic moduli of the dry rock
                * *References* -- ----------
                  - Avseth, P.; Skjei, N. & Mavko, G. The Leading Edge, GeoScienceWorld, 2016, 35, 868-87.















      ..
          !! processed by numpydoc !!


