using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class Target : MonoBehaviour, IDamageable {

    public float health = 1;
    public AudioSource targetSounds;
    public AudioClip impact;
    public GameObject onDestroy; 

    public void TakeDamage(float damage)
    {
        health -= damage;
        if (health <= 0) 
        {
            targetSounds.PlayOneShot(impact);
            Destroy(gameObject);
            Instantiate(onDestroy, transform.position, transform.rotation);

        }
    }
}