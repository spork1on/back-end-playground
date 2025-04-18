using System.Collections;
using System.Collections.Generic;
using System.Numerics;
using UnityEngine;

public class PistolSounds : MonoBehaviour

{   public AudioSource weaponShoot;
    public AudioClip pistolShoot;
    public AudioClip pistolReload;
    public GunData gunData;
    private Animator pistolAnim;

    // Start is called before the first frame update
    void Start()
    {
        pistolAnim = GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {
        if((!gunData.reloading) && (gunData.currentAmmo > 0) && (gunData.currentAmmo < 12))
        {
            if(Input.GetMouseButtonDown(0))
            {
                weaponShoot.PlayOneShot(pistolShoot);
                pistolAnim.SetTrigger("Shoot");
            }
        }
        
        if(gunData.reloading && !weaponShoot.isPlaying)
        {
            weaponShoot.PlayOneShot(pistolReload);
            pistolAnim.SetTrigger("Reload");            
        }
    }
}