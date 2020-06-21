using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[DisallowMultipleComponent]
[RequireComponent(typeof(Collider))]
public class Teleport2 : MonoBehaviour
{
	public float   teleportRange;
	public Vector3 lowerBoundaries, upperBoundaries;
    
	void OnMouseDown()
	{
		Vector3 newPos = transform.position;
        
		newPos = transform.position + new Vector3 (
				Random.Range(-teleportRange, teleportRange),
				Random.Range(-teleportRange, teleportRange),
				Random.Range(-teleportRange, teleportRange)
		);

		newPos.x = Mathf.Clamp(newPos.x, lowerBoundaries.x, upperBoundaries.x);
		newPos.y = Mathf.Clamp(newPos.y, lowerBoundaries.y, upperBoundaries.y);
		newPos.z = Mathf.Clamp(newPos.z, lowerBoundaries.z, upperBoundaries.z);

		transform.position = newPos;
	}
}