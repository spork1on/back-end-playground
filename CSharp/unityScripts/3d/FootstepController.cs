using UnityEngine;
using UnityEngine.TextCore.Text;
public class FootstepController : MonoBehaviour
{
    public AudioClip[] footstepSounds; // Array to hold footstep sound clips
    private float minTimeBetweenFootsteps = 0.7f; // Minimum time between footstep sounds
    private float maxTimeBetweenFootsteps = 1.2f; // Maximum time between footstep sounds

    private AudioSource audioSource; // Reference to the Audio Source component
    private bool isWalking = false; // Flag to track if the player is walking
    public float timeSinceLastFootstep; // Time since the last footstep sound

    private void Awake()
    {
        audioSource = GetComponent<AudioSource>(); // Get the Audio Source component
    }

    private void Update()
    {
        // Check if the player is walking
        if (isWalking)
        {
            // Check if enough time has passed to play the next footstep sound
            if (Time.time - timeSinceLastFootstep >= Random.Range(minTimeBetweenFootsteps, maxTimeBetweenFootsteps))
            {
                // Play a random footstep sound from the array
                AudioClip footstepSound = footstepSounds[Random.Range(0, footstepSounds.Length)];
                audioSource.PlayOneShot(footstepSound);

                timeSinceLastFootstep = Time.time; // Update the time since the last footstep sound
            }
        }
    }

    // Call this method when the player starts walking
    public void StartWalking()
    {
        isWalking = true;
        minTimeBetweenFootsteps = 0.7f;
        maxTimeBetweenFootsteps = 1.2f;
    }

    // Call this method when the player stops walking
    public void StopWalking()
    {
        isWalking = false;
    }

    public void StartRunning()
    {
        minTimeBetweenFootsteps = 0.3f;
        maxTimeBetweenFootsteps = 0.5f;
    }
    
    public void StartCrounching()
    {
        minTimeBetweenFootsteps = 1.0f;
        maxTimeBetweenFootsteps = 2.2f;
    }

}