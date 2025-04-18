using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AimingSystem : MonoBehaviour
{
    public Camera aimCam;
    private float aimFOV = 40;
    private float standardFOV = 60;
    private float t = 12f;

    // Update is called once per frame
    void Update()
    {
        if(Input.GetMouseButton(1))
        {   
            aimCam.fieldOfView = Mathf.Lerp(aimCam.fieldOfView, aimFOV, t * Time.deltaTime);
        }
        else
        {
            aimCam.fieldOfView = standardFOV;
        }
    }
}
