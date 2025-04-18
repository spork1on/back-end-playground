using System.Collections;
using System.Collections.Generic;
using UnityEngine;
 
[RequireComponent(typeof(CharacterController))]
public class FPSController : MonoBehaviour
{
    private FootstepController footStepController;
    public Camera playerCamera;
    private float walkSpeed = 6f;
    private float runSpeed = 10f;
    private float jumpPower = 5f;
    private float gravity = 10f;
 
    public float lookSpeed = 2f;
    public float lookXLimit = 45f;
 
    Vector3 moveDirection = new();
    float rotationX = 0;
 
    public bool canMove = true;
 
    
    CharacterController characterController;
    void Awake()
    {
        characterController = GetComponent<CharacterController>();
        footStepController = GetComponentInChildren<FootstepController>();
        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
    }
 
    void Update()
    {
 
        #region Handles Movement
        Vector3 forward = transform.TransformDirection(Vector3.forward);
        Vector3 right = transform.TransformDirection(Vector3.right);

        //Press Left Control to crouch
        bool isCrounching = Input.GetKey(KeyCode.LeftControl);
        if (isCrounching && characterController.isGrounded)
        {
            runSpeed = 5f;
            walkSpeed = 2.0f;
        }
        else
        {
            runSpeed = 10f;
            walkSpeed = 6f;
        }

        // Press Left Shift to run
        bool isRunning = Input.GetKey(KeyCode.LeftShift);
        float curSpeedX = canMove ? (isRunning && characterController.isGrounded ? runSpeed : walkSpeed) * Input.GetAxis("Vertical") : 0;
        float curSpeedY = canMove ? (isRunning && characterController.isGrounded ? runSpeed : walkSpeed) * Input.GetAxis("Horizontal") : 0;
        float movementDirectionY = moveDirection.y;
        moveDirection = (forward * curSpeedX) + (right * curSpeedY);
        
        if(Input.GetButton("Horizontal") || Input.GetButton("Vertical") && characterController.isGrounded)
        {
            if(isCrounching)
            {
                footStepController.StartCrounching();
            }

            else if (isRunning)
            {
                footStepController.StartRunning();
            }
           
            else
            {
                footStepController.StartWalking();
            }            
        }
        else
        {
            footStepController.StopWalking();
        }

        #endregion
 
        #region Handles Jumping
        if (Input.GetButton("Jump") && canMove && characterController.isGrounded)
        {
            moveDirection.y = jumpPower;
        }
        else
        {
            moveDirection.y = movementDirectionY;
        }
 
        if (!characterController.isGrounded)
        {
            moveDirection.y -= gravity * Time.deltaTime;
        }
 
        #endregion
 
        #region Handles Rotation
        characterController.Move(moveDirection * Time.deltaTime);
 
        if (canMove)
        {
            rotationX += -Input.GetAxis("Mouse Y") * lookSpeed;
            rotationX = Mathf.Clamp(rotationX, -lookXLimit, lookXLimit);
            playerCamera.transform.localRotation = Quaternion.Euler(rotationX, 0, 0);
            transform.rotation *= Quaternion.Euler(0, Input.GetAxis("Mouse X") * lookSpeed, 0);
        }
 
        #endregion
    }
}

